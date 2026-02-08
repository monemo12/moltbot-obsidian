# DEID items.json 規格（Researcher → 寄信）

固定輸出路徑：
- `moltbot-tools/state/daily-econ-invest-digest/items.json`

## 目標
Researcher 讀原文（含英文）後，輸出 **最多 10 則**、**依時間新到舊** 的新聞條目，每則提供 **中文摘要（≤300 字）**。

## JSON 允許的外層格式
兩種都可（建議用 A）：

A) 直接是陣列
```json
[
  {"title":"...","url":"..."}
]
```

B) 包在物件內
```json
{"items":[
  {"title":"...","url":"..."}
]}
```

## 每個 item 欄位
### 必填
- `title`：新聞標題（字串）
- `url`：原文連結（字串）

### 建議填
- `source`：來源名稱（字串；例如 Financial Times / Fed / Yahoo Finance）
- `published`：時間（建議 ISO8601；例如 `2026-02-08T08:30:00Z`；若只知道日期也可 `YYYY-MM-DD`）
- `zh_summary`：中文摘要（字串，≤300 字）

### 例外情況（抓不到全文 / 付費牆）
仍需產出中文摘要，但在摘要結尾加註：
- `（資訊受限：未能取得全文）`

## 範例（建議格式）
```json
[
  {
    "title": "Fed signals...",
    "url": "https://example.com/article",
    "source": "Federal Reserve",
    "published": "2026-02-08T12:10:00Z",
    "zh_summary": "（≤300字）...（資訊受限：未能取得全文）"
  }
]
```
