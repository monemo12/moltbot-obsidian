# Daily Tech Digest (DTD) — Single Source of Truth

## Purpose
Automated tech news digest: fetch RSS/Atom → dedupe → rank/select → generate digest → deliver.

## Current State (authoritative)
- **Status:** MVP working + automated.
- **Schedule:** **Every Thursday 09:00 Asia/Taipei** (cron-driven).
- **Delivery:** Email.

## Delivery Details
- **From:** Jarvis (m16994503@gmail.com)
- **To:** monemo12@gmail.com
- **Timezone:** Asia/Taipei

## Key Decisions
- **Plain text email** (HTML stripped; `<img>` removed) to avoid source HTML/CSS affecting readability.
- **Feed fault tolerance** for broken feeds (e.g., temporary RSS 404) so the pipeline does not hard-fail.
- **Cross-run dedup (7 days)** to prevent the same article appearing on consecutive sends.
  - Dedup window: **last 7 days** (configurable)
  - Behavior on duplicate: **do not show** (filtered out)
  - Keying:
    - Prefer **canonical URL** (remove tracking params like `utm_*`, `fbclid`, `gclid`, etc.; remove fragments)
    - Fallback to **normalized title** when URL is missing
  - Persisted “seen” state is only updated **after a successful real send** (test sends/builds do not pollute state).

## Where Dedup State Lives
- Default: `moltbot-tools/state/daily-tech-digest/seen.json`

## CLI Controls (if needed)
- `--dedup-days N` (default 7)
- `--no-dedup`
- `--seen-file /path/to/seen.json`

## Notable Milestones
- 2026-02-01: Cron job set; first digest successfully sent.
- 2026-02-01: HTML cleaning implemented (commit: `94d6be3`) — MVP achieved.
- 2026-02-08: Added persistent 7-day cross-run dedup (commit: `62c49a3`).

## References
- Config: `moltbot-tools/config/daily-tech-digest.yaml`
- Tool binary: `~/.local/bin/daily-tech-digest`
