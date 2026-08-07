# Оси скоринга

Фиксированные веса. При thin inputs — bands + quotes важнее fake precision.

## Global (все режимы)

```
Overall = 0.25×Evidence
        + 0.20×RoleClarity
        + 0.20×AntiPersonaClean
        + 0.15×TenSecondRead
        + 0.10×KeywordFit
        + 0.10×Structure
```

| Axis | 0.0 | 0.5 | 1.0 |
|------|-----|-----|-----|
| **Evidence** | process/noise | mix; мало PASS | majority PASS/WEAK+ с Z |
| **RoleClarity** | title soup | одна family, grade fuzzy | singular family+grade |
| **AntiPersonaClean** | CLEAR×2+ | PARTIAL 1–2 | NONE / редкий CLEAR |
| **TenSecondRead** | роль/домен/грейд не видны | partial | grade+domain+hook |
| **KeywordFit** | нет target → generic PM density; с JD → coverage high-weight terms | mid | high |
| **Structure** | fails length/chronology/skills water | mixed | passes T или S |

Overall% = round(100×Overall). Показать арифметику.

## MODE 3 — Match per archetype

```
Match = 0.35×CoreCoverage
      + 0.30×AchievementDensity
      + 0.20×DomainMatch
      + 0.15×LanguageAlignment
```

| Component | Определение |
|-----------|-------------|
| CoreCoverage | Σ весов найденных / Σ весов ядра |
| AchievementDensity | PASS / experience bullets |
| DomainMatch | рубрика ниже |
| LanguageAlignment | canonical hits / all term hits |

### DomainMatch (один уровень)
| Score | Смысл |
|------:|--------|
| 1.0 | та же индустрия + тип продукта |
| 0.7 | смежная индустрия или тип |
| 0.4 | тот же B2B/B2C class, другой домен |
| 0.1 | только generic PM transfer |
| 0.0 | несовместимо |

### Веса терминов
```
freq   = JD_с_термином / JD_в_типаже
weight = freq × position × emphasis
position: 1.5 title/first req; 1.2 must-have; 1.0 duties; 0.7 nice-to-have
emphasis: 1.3 повтор 3+ в одном JD; иначе 1.0
```
Канон = majority spelling внутри типажа.

## Density (когда CV разобран)
- Keyword density ≈ canon / content words ×100 (guide 3–6%)  
- Signal/Noise = (PASS+scope) / max(1, FAIL+soft); guide ≥1.5  
- Verb repetition &gt;40% — flag  
- Coverage spread (MODE 3): hard/domain/tasks/exp/scale — flag max−min &gt;50 pp  

## Bands
| Overall% | Label |
|---------:|--------|
| ≥75 | competitive for stated target |
| 50–74 | conditional — major gaps |
| &lt;50 | rework positioning/search before volume |
