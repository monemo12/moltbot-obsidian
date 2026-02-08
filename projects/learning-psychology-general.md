# General Psychology Learning System (SSoT) — Annie

## Purpose
A long-term, low-friction General Psychology (“普通心理學”) learning system built from `LEARNING_SYSTEM_TEMPLATE.md`.

## Canonical Primary Source (2026-02-07)
- **OpenStax — Psychology 2e** (primary, authoritative textbook; free and linkable)
  - Preface: https://openstax.org/books/psychology-2e/pages/preface
  - Chapter 1: https://openstax.org/books/psychology-2e/pages/1-introduction
- Policy: weekly materials + Anki cards should be derived from this book first; supplementary links are optional and should be clearly marked as supplementary.

Related governance SSoT: `projects/learning-system-builder-template.md`.

## Current State (authoritative)
- **Status:** System scaffold + Week 1 package ready.
- **Daily cadence:** 15 minutes/day (Anki + content + optional reflection).
- **Progress:** Week 0 (prep) → starting **Module 1 / Unit 1.1**.
- **Tracking:** Manual weekly check-in + `progress.md`.

## Annie’s Preferences / Constraints
- **Goal:** Understand core concepts + apply to real-life observations.
- **Language:** EN primary + ZH support (bilingual).
- **Mode:** Mixed (curated resources + AI-generated summaries).
- **SRS:** Anki.
- **Reminders:** Not needed; **weekly check-in** is the main sync point.
- **Key constraint (2026-02-07):** If there is no separate reading material, Anki cards must **not** be “orphan vocabulary”. Each key term/comparison card should include minimal background + a contrast cue so Annie can answer comparison questions.

## Learning Path
- 5 modules / ~20 weeks at 15 min/day.
- Current module: **Module 1 — Foundations & Research Methods**

(Full path is maintained in `learning-systems/psychology-general/system.md`.)

## Daily Routine (15 min)
- 3 min: Anki review
- 8 min: New content (reading/video)
- 2 min: New cards
- 2 min: Quick reflection (optional)

## Week 1 Package (Unit 1.1)
- Objectives + materials + checkpoint in: `learning-systems/psychology-general/resources.md`
- Importable cards (18): `learning-systems/psychology-general/anki/week-01.txt`

## Progress / Review
- Progress log: `learning-systems/psychology-general/progress.md`
- Weekly review questions focus on:
  - studied how many days?
  - what concepts still fuzzy?
  - can you explain key ideas in your own words?
  - readiness to move on / adjust pace

## Anki Delivery Policy (current)
- **Source-of-truth for card content:** `.txt` files under `learning-systems/psychology-general/anki/`
- **Weekly delivery (current): Email**
  - Weekly cron regenerates/collects the latest `.apkg` (and the latest `.txt` if present) and **emails it to Annie**.
  - Telegram group delivery is **disabled** for the weekly package.
- **We prefer reliability over heavy automation.**
  - If anything goes wrong, `.txt` remains the fallback import path.
- Card format: `Front[TAB]Back[TAB]tags`

### Card Authoring Guideline (comparison-first)
- When a card is a **comparison** (X vs Y), always include:
  1) **Comparison axis** (e.g., structure vs function)
  2) **Cue words** (what to look for in questions)
  3) (Optional) 1 mini-example or “fits which perspective?” quick check
- When a prompt is **enumerative** (e.g., “give 2 perspectives / list 3 factors / name 4 examples”), write the **main items + a concrete example for each** in the back side so the card is easy to expand/shrink (swap-in/out) without losing coverage.
- When a prompt feels **too slogan-like** (“what did X bring back/lead to/why did X matter?”) and you understand the sentence but not the *logic*, add a **causal scaffold** to the back:
  - **Main**: 1-sentence direct answer
  - **Before**: what was the previous dominant view, and what did it exclude?
  - **Bridge**: what methods/ideas made the new claim testable?
  - **After**: what topics/practices became legitimate or mainstream as a result?
- Avoid pure definition-only cards for abstract schools/terms.

## Key References
- System design: `learning-systems/psychology-general/system.md`
- Resources: `learning-systems/psychology-general/resources.md`
- Progress: `learning-systems/psychology-general/progress.md`
- Cards: `learning-systems/psychology-general/anki/week-01.txt`
- Weekly email sender CLI (repo): `moltbot-tools/packages/python/psychology_material/`
