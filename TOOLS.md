# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## Cron Jobs - Delivery Rules

**方案 3：依任務類型分流**

- 📧 **私訊給 Annie**（`to: "6968309478"`）：
  - 科技日報
  - 個人提醒
  - 敏感/私密通知

- 👥 **Jarvis Bot 群組**（`to: "-5137119242"`）：
  - 天氣報告
  - 公開提醒
  - 可分享的通知

---

Add whatever helps you do your job. This is your cheat sheet.
