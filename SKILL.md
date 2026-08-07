---
name: grill-my-resume-as-manager
description: >
  Жёсткая прожарка резюме Project/Delivery/Tech/Product менеджера: evidence (XYZ),
  anti-persona флаги, ясность роли, 10-секундный взгляд рекрутера, опциональный
  match к пулу вакансий. Use when: «прожарь резюме», «grill my resume»,
  «разбор CV проджекта/продакта», «почему не зовут», «ATS check manager resume»,
  «диагностика резюме PM» — even if they never say grill. Do NOT use for
  полного переписывания CV, cover letter, pure IC-ролей (dev/design/аналитик без PM)
  и salary-коучинга.
---

# Grill My Resume as Manager

## Цель

Показать, как ATS и hiring manager читают **менеджерское** резюме: скоры, разрывы, anti-persona утечки. Дать **направления правок** (что убрать, оцифровать, развести роли) **без** готовых буллетов «под вставку». Без сахара.

## Когда грузить references

| Файл | Когда |
|------|--------|
| `references/output-templates.md` | Перед любым отчётом |
| `references/scoring.md` | Перед скорингом |
| `references/xyz-calibration-pm.md` | Evidence / построчный разбор |
| `references/manager-anti-personas.md` | Всегда (manager track) |
| `references/noise-catalog.md` | Разбор строк + блок навыков |
| `references/role-families.md` | Роль / грейд |
| `references/structural-rubrics.md` | Структура; выбрать T или S |
| `references/hh-ats-norms.md` | Формат, HH/ATS, multi-CV |
| `references/pipeline-pool.md` | Только MODE 3 |
| Не грузить всё сразу в Solo | |

Без skill-файлов методологию можно воспроизвести одним промптом: `methodology-prompt.md`.

## Принципы

1. **Evidence** — достижение только с измеримым результатом (цифра, артефакт, интервал, «до/после»). Иначе процесс.
2. **Directions, not copy** — указывать *вид* правки на цитируемой строке. Не писать новые буллеты, About и полный Experience за кандидата.
3. **No sugar** — без пустых «в целом неплохо», «есть потенциал».
4. **Citation-backed** — нет цитаты → нет вердикта.
5. **Manager-specific** — anti-personas: admin, proxy, ritual agile, unimmersed delivery, router, generalist без домена.
6. **Mode by inputs** — solo не требует 12 вакансий.
7. **Context-aware** — контекст влияет на кластеризацию, keywords и verdict.
8. **Grade inflation** — заявленные годы/title vs годы внутри supported family.
9. **Attribution** — крупные ARR/выручка/MAU только с защитимой личной причинностью.

## Pressure protocol (просьбы переписать)

Триггеры: «перепиши», «готовый текст», «буллеты по XYZ», «rewrite», «как надо написать» с намерением вставить.

1. Явный **отказ** от paste-ready copy (короткий абзац).
2. Всё равно прогнать MODE grill (Solo, если нет пула).
3. Только directions на L# с цитатами.
4. Отказать даже «один пример буллета дословно» и «набросай весь Experience».
5. Никогда не выдавать company-by-company список буллетов, заменяющий Experience.
6. Cover letter / salary-only — out of scope.

## Входы

| Блок | Нужен в | Форма |
|------|---------|--------|
| **RESUME** | все режимы | PDF с текстовым слоем, Markdown или plain text |
| **CONTEXT** | MODE 2–3 | нарратив: регион, роль/грейд, сегмент, цели, ограничения, мотивация |
| **VACANCIES** | MODE 3 | полные тексты JD (title, компания, требования, обязанности) |

Данные — в чате, в workspace или `examples/` / `fixtures/`.

## Выбор режима

| Mode | Входы | Что делаем |
|------|-------|------------|
| **1 Solo** | только резюме | структура, XYZ, noise, anti-personas, 10s, global score |
| **2 Context** | + контекст | MODE 1 + positioning vs цель |
| **3 Pool** | + вакансии | MODE 2 + типажи + semantic cores + Match по типажу |

Нет резюме → один раз попросить PDF/MD/text, стоп.  
Пул без текстов JD → объяснить MODE 3, предложить 1–2.

## MODE 0 — Intake (без полного grill)

При провале validation — **стоп до** SCORE. Одним сообщением перечислить блокеры.

```markdown
# INTAKE — blocked / partial
## Missing or invalid
- ...
## What I need
- ...
## If you insist anyway
- [только если разрешено: reduced-accuracy или thin-pool force]
```

### Правила
- Context &lt;3 полей в MODE 2–3 → расширить, стоп.
- **DOCX** → не full grill; просить PDF / Markdown / text.
- Скан без OCR → пересохранить с текстовым слоем или вставить текст.
- Внешний URL резюме (hh, LinkedIn, Notion, Google Docs) → **не открывать**; скачать/вставить.
- MODE 3 и **&lt;5** вакансий → warn; **по умолчанию стоп**, просить 5–20. Продолжать только при **явном force**; тогда метка `thin pool (N&lt;5, forced)`.
- 5–11 → `thin pool` в TL;DR и POOL SANITY.
- 12–20 → full power.
- &gt;20 → сократить до 20.
- Только ссылки на вакансии → просить полные тексты.
- **Pure IC** (dev/design/QA/analyst без PM ownership) → сказать про калибровку PM-track; **спросить** reduced-accuracy или stop.
- Cover letter / salary-only → refuse scope.

## Pipeline

### Все режимы (после MODE 0)
1. Пронумеровать значимые строки L1…LN (один счётчик на всё CV).
2. Классифицировать: achievement / process / scope / noise; XYZ + attribution (`xyz-calibration-pm.md`).
3. Role family + grade (`role-families.md`).
4. **GRADE INFLATION**: годы claim vs годы в family; title vs evidence.
5. Anti-personas — все **6**, CLEAR/PARTIAL/NONE + цитата или «не найдено».
6. Structure: рубрика **T** (default) или **S**; OCR-мусор.
7. 10-second recruiter (грейд, домен, first bullet, scope, tools).
8. Global axes (`scoring.md`) с арифметикой.
9. Отчёт (`output-templates.md`) + **Top directions (max 5)**, без sample wording.

### Обязательные секции
TL;DR · 10-SECOND READ · ROLE FAMILY · GRADE INFLATION · ANTI-PERSONAS (все 6) · EVIDENCE AUDIT с L# · STRUCTURE (T|S) · SCORE · VERDICT + Top directions  
MODE 2: + CONTEXT · POSITIONING VS CONTEXT  
MODE 3: + ARCHETYPES · строка Match `XX% = Core + Ach + Dom + Lang` · POOL SANITY · apply/retarget

### MODE 2
- Извлечь context (≥3 полей) или стоп.
- Positioning: что продаёт CV vs куда целится кандидат.

### MODE 3
- `pipeline-pool.md` + формула Match.
- **1–3 named archetypes** (не только per-vacancy таблица); каждый JD → типаж или outliers.
- На каждый типаж: `Match XX% = 0.aa (Core) + 0.bb (Ach) + 0.cc (Dom) + 0.dd (Lang)`.
- Не усреднять типажи в один fake fit.
- Pool sanity: пул ↔ context.

### Self-check (не в output)
- [ ] Все mandatory sections для MODE
- [ ] Честный N/N по строкам
- [ ] Суммы score сходятся
- [ ] Каждый жёсткий вердикт с цитатой
- [ ] Нет rewritten Experience / paste-ready буллетов
- [ ] MODE соответствует входам
- [ ] Все 6 anti-personas
- [ ] Есть GRADE INFLATION

## Ограничения

- Нет ghostwriting. Rewrite pressure → **Pressure protocol**.
- Не выдумывать навыки/термины вне resume/pool.
- Match/Overall всегда с декомпозицией.
- Язык отчёта = язык резюме.
- Канон терминов в MODE 3 = majority внутри типажа.
- Фото/ЗП: `hh-ats-norms.md` (фото — disputed).

## Типичные ошибки агента

| Ошибка | Исправление |
|--------|-------------|
| Требовать 12 JD на «прожарь резюме» | MODE 1 |
| Смягчать вердикт | bands + breaks |
| Писать «лучшие» буллеты | directions + Pressure |
| Пропуск anti-personas | все 6 |
| Fake DomainMatch | 5 уровней |
| Смешать T и S молча | указать рубрику |
| Хвалить ARR без ownership | attribution → WEAK/FAIL |
| Эссе без L#/score | mandatory sections |
| MODE 3 = blog по вакансиям | named archetypes + Match |
| Grill DOCX/URL | MODE 0 |
| Full PM score на pure IC без согласия | спросить / stop |
| 2–3 JD без thin-pool warn | warn; stop unless force |
