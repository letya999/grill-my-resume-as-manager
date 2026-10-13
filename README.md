<p align="center">
  <strong>English</strong> · <a href="README.ru.md">Русский</a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="License: MIT"></a>
  <a href="https://skills.sh/letya999/grill-my-resume-as-manager"><img src="https://skills.sh/b/letya999/grill-my-resume-as-manager" alt="skills.sh"></a>
</p>
# Grill My Resume as Manager

Open skill for a **hard grill** of Project / Delivery / Tech / Product manager resumes.

Not a ghostwriter. The agent scores evidence (XYZ), flags manager anti-personas (admin, proxy, ritual agile, …), checks 10-second recruiter read, and optionally matches a vacancy pool. It gives **fix directions** without writing replacement bullets.

## Modes

| Mode | You provide | You get |
|------|-------------|---------|
| **1 Solo** | resume | full grill + score + directions |
| **2 Context** | resume + “where I’m going” narrative | + positioning vs target |
| **3 Pool** | resume + context + 5–20 full JD texts | + archetypes + per-cluster match % |

## Install

```bash
npx skills add letya999/grill-my-resume-as-manager
```

```bash
# Gemini CLI / Open Skills style
gemini skills install ./grill-my-resume-as-manager.skill
```

Or point Claude Code / Cursor / Grok at `SKILL.md`:

> Use grill-my-resume-as-manager on examples/resume.pdf (solo grill)

## Example data

`examples/` — sample context, resume PDF, and 12 vacancy texts for MODE 3 drills.

## Package layout

```
grill-my-resume-as-manager/
  SKILL.md
  references/     # load on demand (see SKILL map)
  examples/       # fixtures, not required at runtime
  package.json
  LICENSE
```

## Philosophy

Evidence rule: no measurable result → process, not achievement. Market stops buying harness/admin PMs; the skill names those leaks with quotes.
