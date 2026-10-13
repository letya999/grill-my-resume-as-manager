# MODE 3 pipeline detail

Load only in MODE 3 (pool grill).

## Step order
1. Context extraction (≥3 of: region, role/grade, segment, targets, constraints, motivation) or stop.
2. Archetype clustering: 1–3 **named** clusters by role type, segment, industry, company size, grade, domain focus.
   - Vacancies outside user target_role/grade → outliers, not a fourth archetype.
   - If 4+ natural clusters → keep top 3 by size; rest outliers.
   - A per-vacancy commentary table is optional **extra**, not a substitute for named archetypes.
3. Emit for each archetype a single score line before deep dive:
   `A: Name — Match XX% = 0.aa (Core) + 0.bb (Ach) + 0.cc (Dom) + 0.dd (Lang) — vacancy #ids`
4. Semantic core per archetype: mine terms across 5 classes (checklist, not all dumped to user):
   - hard skills/tools
   - domain/industry
   - task types
   - experience requirements (years, company types, grade, languages)
   - scale metrics (team, budget, MAU, ARR, …)
   Target **25–40 terms** per core when archetype has 5+ vacancies; if fewer, re-mine.
   Weights: see `scoring.md`.
5. Line-by-line resume parse (all significant lines numbered L1…LN once across whole CV).
6. Score per archetype (`scoring.md` Match formula) — rewrite the score lines from step 3 with final numbers.
7. Density metrics.
8. Structural audit via chosen rubric + grade inflation.
9. 10-second recruiter checks.
10. Anti-personas (all six) + systemic issues.
11. Self-check then emit template from `output-templates.md`.

## Clustering example
15 vacancies: 8 Senior PM bank/telecom SAFe high-load; 4 PM outsource RFP; 2 Head of Product B2B SaaS; 1 Scrum Master gamedev.
→ Archetypes: Enterprise Delivery (8), Outsource Delivery (4), Product Lead (2). Gamedev SM → outlier.
