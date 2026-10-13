# Repository instructions

This repository maintains one portable Agent Skill: `grill-my-resume-as-manager`.
It is a hard diagnostic for Project/Delivery/Tech/Product manager resumes.
All maintained repository content is written in English except `README.ru.md`,
the Russian translation — keep the two in sync.

## Read before editing

Read [SKILL.md](SKILL.md), [README.md](README.md), and the loaded-on-demand
files under `references/`. `examples/` and `fixtures/` are eval data, not
runtime requirements.

## Preserve the role

- Directions, not copy: the skill gives fix directions and never writes
  replacement bullets, About sections, or full Experience for the candidate.
- No sugar, citation-backed verdicts only: no quote → no verdict.
- Keep the mode-by-inputs design: solo must not require a vacancy pool.
- Do not add ghostwriting, cover-letter generation, or salary coaching.

## Validation

```bash
python -m unittest discover -s scripts -p "test_*.py" -v 2>/dev/null || true
```

Check eval fixtures still parse after changing scoring or templates; keep
`evals/evals.json` IDs stable.

## Safety

- Never commit `.env`, tokens, or real candidate personal data beyond the
  anonymized fixtures already in `fixtures/`.
- See [SECURITY.md](SECURITY.md) for vulnerability reporting.
