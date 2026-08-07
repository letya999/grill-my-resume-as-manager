# -*- coding: utf-8 -*-
"""Collect PM-like PDFs and write anonymized text fixtures."""
from __future__ import annotations

import hashlib
import re
import shutil
from pathlib import Path

from pypdf import PdfReader

SEARCH_ROOTS = [
    Path(r"C:\Users\User\Downloads\Telegram Desktop"),
    Path(r"C:\Users\User\Downloads"),
]
OUT_DIR = Path(__file__).resolve().parents[1] / "fixtures" / "resumes"
MAX_N = 20
MAX_BYTES = 4 * 1024 * 1024

NAME_HINT = re.compile(
    r"(?i)(cv|resume|резюме|curriculum|portfolio)|"
    r"(project[\s_\-]?manager|product[\s_\-]?manager|delivery)|"
    r"(руководитель[\s_\-]?проект)|"
    r"([A-ZА-Я][a-zа-яё]+[\s_\-][A-ZА-Я][a-zа-яё]+)"
)
SKIP = re.compile(
    r"(?i)(receipt|invoice|transfer|pitch|deck|brochure|workshop|"
    r"kanban.?guide|sutton|report|statement|certificate|offer|"
    r"curestry|twinby|presentation|скрин|program|программ)"
)

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?:\+7|8)[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}"
)
TG_RE = re.compile(r"@[\w_]{3,32}")
URL_RE = re.compile(r"https?://\S+")
# crude "First Last" at line starts (RU/EN)
PERSON_LINE = re.compile(
    r"(?m)^[\s]*([А-ЯA-Z][а-яa-zё]+(?:\s+[А-ЯA-Z][а-яa-zё]+){1,3})\s*$"
)


def score_path(p: Path) -> int:
    n = p.name
    if SKIP.search(n):
        return -100
    s = 0
    if re.search(r"(?i)\b(cv|resume|резюме)\b", n):
        s += 50
    if re.search(r"(?i)(project|product|delivery|manager|pm|руководитель|проджект|продакт)", n):
        s += 30
    if NAME_HINT.search(n):
        s += 10
    if p.suffix.lower() != ".pdf":
        return -100
    if p.stat().st_size > MAX_BYTES:
        s -= 20
    return s


def extract_text(pdf: Path) -> str:
    try:
        r = PdfReader(str(pdf))
        parts = []
        for page in r.pages[:8]:
            parts.append(page.extract_text() or "")
        return "\n".join(parts).strip()
    except Exception as e:
        return f"[EXTRACT_ERROR] {e}"


def anonymize(text: str, stub: str) -> str:
    t = EMAIL_RE.sub(f"{stub.lower()}@example.invalid", text)
    t = PHONE_RE.sub("+7 (900) 000-00-00", t)
    t = TG_RE.sub(f"@{stub.lower()}_tg", t)
    t = URL_RE.sub("https://example.invalid/profile", t)
    # replace first-looking person name lines
    def repl_person(m: re.Match) -> str:
        name = m.group(1)
        if len(name) < 5:
            return m.group(0)
        # skip if looks like company/section
        low = name.lower()
        if any(x in low for x in ("manager", "project", "product", "опыт", "навык", "образован")):
            return m.group(0)
        return f"Кандидат {stub}"

    t = PERSON_LINE.sub(repl_person, t, count=5)
    # common header patterns "Имя Фамилия" in first 400 chars
    head = t[:400]
    head2 = re.sub(
        r"[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?",
        f"Кандидат {stub}",
        head,
        count=2,
    )
    t = head2 + t[400:]
    return t


def main() -> None:
    candidates: list[tuple[int, Path]] = []
    seen: set[str] = set()
    for root in SEARCH_ROOTS:
        if not root.exists():
            continue
        for p in root.rglob("*.pdf"):
            try:
                key = p.name.lower()
                if key in seen:
                    continue
                sc = score_path(p)
                if sc < 20:
                    continue
                seen.add(key)
                candidates.append((sc, p))
            except OSError:
                continue
    candidates.sort(key=lambda x: (-x[0], x[1].stat().st_size))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # wipe old
    for old in OUT_DIR.glob("*"):
        if old.is_file():
            old.unlink()

    manifest = []
    picked = 0
    for sc, p in candidates:
        if picked >= MAX_N:
            break
        text = extract_text(p)
        if len(text) < 200 or text.startswith("[EXTRACT_ERROR]"):
            continue
        # need some PM/work signal
        if not re.search(
            r"(?i)(project|product|manager|опыт|обязан|достиж|jira|scrum|команд|delivery|руководитель)",
            text,
        ):
            continue
        picked += 1
        stub = f"P{picked:02d}"
        anon = anonymize(text, stub)
        h = hashlib.sha256(p.name.encode("utf-8", errors="replace")).hexdigest()[:10]
        out_name = f"resume_{stub}_{h}.txt"
        (OUT_DIR / out_name).write_text(anon, encoding="utf-8")
        manifest.append(
            {
                "id": stub,
                "file": out_name,
                "source_name_hash": h,
                "score": sc,
                "chars": len(anon),
                "note": "source filename and personal data removed/redacted",
            }
        )
        print(f"OK {stub} score={sc} chars={len(anon)} from_hash={h}")

    import json

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote {picked} resumes to {OUT_DIR}")


if __name__ == "__main__":
    main()
