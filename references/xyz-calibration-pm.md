# XYZ calibration for PM / Delivery / Product manager bullets

## Rule
An achievement exists only with measurable result: number, artifact, interval, or explicit before/after. Without that — process or scope-statement, not achievement.

## XYZ
- **X** — strong verb + object (what you did)
- **Y** — change produced (what moved)
- **Z** — metric / artifact / time window

Framework preference in this skill: **XYZ** (not STAR). STAR is acceptable only if X+Y+Z are still explicit.

## Line types
| Type | Definition | XYZ? |
|------|------------|------|
| achievement | candidate-caused outcome | score PASS/WEAK/FAIL |
| process | activity without outcome | not PASS |
| scope-statement | career fact (team size, title, transfer) | list separately; not achievement |
| noise | soft claim / filler | flag |

## Calibration (use as ground truth)

| Line | Verdict | Why |
|------|---------|-----|
| "Управлял командой 8 разработчиков" | FAIL | X only; headcount is scope |
| "Координировал миграцию монолита силами 8 dev, релиз 2 нед → 2 дня" | PASS | X+Y+Z |
| "Работал в команде, где MAU 100k→500k" | FAIL | metric not attributed to candidate |
| "Увеличил конверсию на 15%" | WEAK | no baseline, no window |
| "Провёл CustDev-интервью" | WEAK/process | process without outcome |
| "Способствовал утроению выручки" | FAIL | contribution not attributed |
| "Перешёл из Android Developer в PM" | SCOPE | not XYZ |
| "Моя суперсила — разруливать кризисы" | NOISE | marketing without artifact |
| "Расширил команду с 5 до 18" | WEAK/scope | growth without business effect |
| "Настроил Jira + Confluence для прозрачности" | process/noise | tool hygiene, no business Z |
| "Провёл ретро и демо, повысил вовлечённость" | WEAK/fail | soft outcome, no measure |
| "Вёл дейли/груминги/планирования" | process | ritual anti-persona signal |
| "Сократил time-to-market на 25% внедрением Scrum" | WEAK | needs baseline window + what actually changed in flow |
| "Руководил продуктами в топ-15 интеграторе с оборотом 40 млрд" | FAIL as achievement | employer prestige / parent GMV — not personal Y/Z |
| "Launched product: €1.5M ARR, 35 enterprise customers" | WEAK unless ownership | PASS only if personal causal role is explicit (owned P&L / led GTM / closed deals); else WEAK + attribution flag |

## Attribution tests
Ask for every number:
1. Is the candidate the causal agent (not "the team/company did")?
2. Is the unit business-relevant for the target role (delivery speed, quality, money, risk, adoption)?
3. Would this impress *this* hiring manager archetype (product vs platform vs enterprise delivery)?
4. Is the number **employer vanity** (holding revenue, "top-N vendor", market rank) rather than project outcome?
5. Could the candidate defend the metric in a 10-minute interview grill without hand-waving?

## Chat-derived hard rules
- Team size alone is **not** an achievement.
- "Улучшил качество на N%" without definition of quality → WEAK.
- Parallel soft stacks ("ответственный, коммуникабельный, проактивный") → noise, not skills.
- Relative lifts on tiny bases ($6k/mo ×3) need absolute context or stay WEAK for senior bars.
