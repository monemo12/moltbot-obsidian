# Daily Econ & Investing Digest (DEID) — Single Source of Truth

## Purpose
Automated econ/investing news digest: fetch RSS/Atom → dedupe → rank/select → generate digest → deliver.

## Current State (authoritative)
- **Status:** Setting up.
- **Schedule:** **Every day 21:00 Asia/Taipei** (cron-driven).
- **Delivery:** Email.

## Delivery Details
- **From:** Jarvis (m16994503@gmail.com)
- **To:** monemo12@gmail.com
- **Timezone:** Asia/Taipei

## Content Scope
綜合：**總經（央行/通膨/就業/匯率）＋市場（股/債/原物料）＋重大事件**

## Key Decisions
- **Plain text email** + HTML email（同一份內容）
- **Feed fault tolerance**：單一來源壞掉不影響整體寄送
- **Cross-run dedup (7 days)**：避免 7 天內重複出現同一篇
  - Persisted “seen” state only updates **after a successful real send**

## Where Dedup State Lives
- `moltbot-tools/state/daily-econ-invest-digest/seen.json`

## CLI Controls (used by cron)
- Tool: `daily-tech-digest`（共用程式；以不同 config 驅動）
- Config: `moltbot-tools/config/daily-econ-invest-digest.yaml`
- Seen: `--seen-file moltbot-tools/state/daily-econ-invest-digest/seen.json`

## References
- Config: `moltbot-tools/config/daily-econ-invest-digest.yaml`
