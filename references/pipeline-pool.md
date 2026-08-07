# MODE 3 — детальный pipeline

Грузить только в MODE 3.

## Порядок
1. Context (≥3 полей) или стоп.  
2. Кластеризация 1–3 **named** типажей (роль, сегмент, индустрия, size, grade, domain).  
   - Вне target_role/grade → outliers.  
   - 4+ кластера → top-3 по размеру; rest outliers.  
   - Per-vacancy commentary — optional extra, **не** замена named archetypes.  
3. Черновая score-строка на типаж:  
   `A: Name — Match XX% = 0.aa (Core) + 0.bb (Ach) + 0.cc (Dom) + 0.dd (Lang) — #ids`  
4. Semantic core: 5 классов (hard / domain / tasks / experience / scale).  
   25–40 терминов при ≥5 JD в типаже. Веса — `scoring.md`.  
5. Line-by-line L1…LN.  
6. Финальный Match (`scoring.md`).  
7. Density.  
8. Structure + grade inflation.  
9. 10-second.  
10. Anti-personas (все 6) + systemic.  
11. Self-check → `output-templates.md`.

## Пример кластеризации
15 JD: 8 Senior PM bank/telecom SAFe; 4 PM outsource RFP; 2 Head of Product SaaS; 1 Scrum Master gamedev.  
→ Enterprise Delivery (8), Outsource Delivery (4), Product Lead (2). Gamedev SM → outlier.
