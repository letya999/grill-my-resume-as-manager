# Scoring axes

Fixed weights for reproducibility across runs. Prefer **bands + quotes** over fake precision when inputs are thin.

## Global axes (all modes)

```
Overall = 0.25*Evidence
        + 0.20*RoleClarity
        + 0.20*AntiPersonaClean
        + 0.15*TenSecondRead
        + 0.10*KeywordFit
        + 0.10*Structure
```

| Axis | 0.0 | 0.5 | 1.0 |
|------|-----|-----|-----|
| **Evidence** | process/noise dominate | mix; few PASS XYZ | majority experience bullets PASS/WEAK+ with Z |
| **RoleClarity** | title soup / family conflict | mostly one family, grade fuzzy | singular family+grade, narrative coheres |
| **AntiPersonaClean** | CLEAR on 2+ anti-personas | PARTIAL on 1–2 | NONE/CLEAR rare |
| **TenSecondRead** | role/domain/grade not visible | partial | grade+domain+hook visible |
| **KeywordFit** | no target → score from generic PM lexicon density only; with JD → core term coverage | mid | high coverage of high-weight terms |
| **Structure** | fails length/chronology/skills water | mixed | passes chosen rubric T or S |

Report each axis 0.00–1.00 and Overall as percent = round(100*Overall).

## MODE 3 only — per-archetype Match

```
Match = 0.35*CoreCoverage
      + 0.30*AchievementDensity
      + 0.20*DomainMatch
      + 0.15*LanguageAlignment
```

| Component | Definition |
|-----------|------------|
| CoreCoverage | sum(weights of core terms found) / sum(weights of core) |
| AchievementDensity | PASS bullets / experience bullets |
| DomainMatch | rubric below |
| LanguageAlignment | canonical-form hits / all term hits |

### DomainMatch rubric (pick one level; do not invent continuous "distance")
| Score | Meaning |
|-------|---------|
| 1.0 | same industry + product type as archetype |
| 0.7 | adjacent industry or adjacent product type |
| 0.4 | same broad B2B/B2C class, different domain |
| 0.1 | only generic PM skill transfers |
| 0.0 | incompatible |

### Term weights (archetype core)
```
freq   = vacancies_with_term / vacancies_in_archetype
weight = freq * position * emphasis
position: 1.5 title/first req para; 1.2 must-have; 1.0 duties; 0.7 nice-to-have
emphasis: 1.3 term repeats 3+ in one JD; else 1.0
```
Canonical form = majority spelling inside the archetype (no forced RU↔EN translation).

## Density metrics (all modes when resume parsed)
- Keyword density ≈ canon hits / content words * 100 (guide band 3–6%; not a hard gate)
- Signal/Noise = (PASS + scope) / max(1, FAIL + soft-noise); guide ≥ 1.5
- Verb repetition: top-3 experience verbs share; flag if >40%
- Coverage spread (MODE 3): hard / domain / tasks / experience / scale — flag if max-min > 50 pp

## Bands for verdict language
| Overall % | Label |
|-----------|--------|
| ≥75 | competitive for stated target (still list gaps) |
| 50–74 | conditional — major gaps before mass apply |
| <50 | rework positioning or search before volume apply |
