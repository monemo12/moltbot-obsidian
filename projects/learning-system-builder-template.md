# Learning System Builder Template (SSoT)

## What this is
A reusable template for building **personalized, theory-driven learning systems** for any domain (not just a one-off study plan).

## Canonical file (source)
- Template content lives here: `LEARNING_SYSTEM_TEMPLATE.md`
- Current template version (inside file): **v2.0**

## When Jarvis should use it (trigger rules)
Use this template automatically when Annie asks to:
- start learning a new domain/skill
- update learning materials / curriculum / learning path / SRS cards
- “幫我規劃怎麼學” / build a learning system

## Core structure (4 phases)
1) **Needs Assessment**（需求診斷）
2) **Theoretical Framework**（學習理論選擇）
3) **System Components**（組件設計：path / daily routine / SRS / tracking）
4) **Maintenance**（維護優化：weekly/monthly review + pace rules）

## Required questions in diagnosis (minimum set)
From the perspective of “**start tomorrow**”:
- Scope boundary (子領域/主題)
- Success definition (達標標準)
- Resource preferences (language/platform; AI-generated vs curated vs mixed)
- Tooling (SRS: Anki/Markdown/other; where progress lives)
- Interaction mechanism (reminders; check-in frequency)
- Getting stuck protocol (switch method / skip / downgrade; who triggers)
- Evaluation criteria (how to decide a unit is learned)

## Related deep-dive memos (context / history)
- `memory/2026-02-02-learning-framework.md`
- `memory/2026-02-03-learning-framework.md`

## Live systems built from this template
- Psychology (General): `projects/learning-psychology-general.md`
  - Implementation folder: `learning-systems/psychology-general/`

## Maintenance policy
- This doc is the **SSoT for governance** (what/when/how we use the template).
- The template itself stays in `LEARNING_SYSTEM_TEMPLATE.md`.
- If the template changes materially (structure/questions/output files), update:
  1) `LEARNING_SYSTEM_TEMPLATE.md`
  2) this SSoT doc (what changed + why)
  3) optionally add a short deep-dive memo under `memory/` if the rationale is non-trivial.
