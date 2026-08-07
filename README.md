# Grill My Resume as Manager

Open Skill: **жёсткая прожарка** резюме Project / Delivery / Tech / Product менеджера.

Не ghostwriter. Скоринг evidence (XYZ), anti-personas, 10-секундный skim, опционально match к пулу вакансий. **Directions** без готовых буллетов.

## Режимы

| Mode | Вход | Результат |
|------|------|-----------|
| 0 Intake | битый input | что исправить во входе |
| 1 Solo | резюме | полный grill |
| 2 Context | + «куда иду» | + positioning |
| 3 Pool | + 5–20 JD | + типажи + Match% |

## Установка

```bash
# Open Skills / Gemini CLI
gemini skills install ./grill-my-resume-as-manager.skill
```

Или укажи агенту `SKILL.md`:

> Используй grill-my-resume-as-manager на examples/resume.md

## Без skill-файлов

Один промпт с той же методологией: **`methodology-prompt.md`** — вставь в любой чат + резюме.

## Содержимое

- `SKILL.md` + `references/` — skill  
- `methodology-prompt.md` — one-shot промпт  
- `examples/` — **синтетические** demo-данные  
- `fixtures/resumes/` — анонимизированные тексты (P01…P20) для локальных тестов  

## Философия

Evidence rule: нет измеримого результата → процесс, не достижение.  
Рынок не покупает harness/admin PM; скилл называет такие утечки цитатами.

## Лицензия

MIT
