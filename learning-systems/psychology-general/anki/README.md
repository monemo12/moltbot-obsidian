# Anki 卡片管理（簡易版）

## 📦 簡化方案

**舊方式（已移除）**：自動同步到 AnkiWeb  
**新方式**：每週產生 `.apkg` 檔案並傳送到 Telegram

## 🔧 檔案說明

- `week-01.txt` - 卡片內容（Tab 分隔：正面 ⇄ 背面）
- `create_apkg_v2.py` - 產生 `.apkg` 檔案的工具
- `.ankiweb_config` - AnkiWeb 帳號配置（保留但不使用）

## 🤖 自動化

**Cron Job**：每週日 12:00（台北時間）
- 自動產生/更新最新的 `.apkg` 檔案
- **以 Email 寄給 Annie**（Telegram 群組寄送已停用）
- Annie 收到後手動匯入即可

## ✋ 手動使用

如果需要手動產生 `.apkg`：

```bash
cd learning-systems/psychology-general/anki
python3 create_apkg_v2.py week-01.txt output.apkg
```

## 📝 新增卡片

1. 建立新的 `week-XX.txt` 檔案
2. 格式：每行一張卡片，Tab 分隔正反面
   ```
   What is Psychology?	The scientific study of mind and behavior
   Who founded behaviorism?	John B. Watson
   ```
3. 等週日自動產生，或手動執行 `create_apkg_v2.py`

## 🧹 移除的檔案

為了簡化系統，已移除：
- 所有自動同步相關腳本
- AnkiConnect 相關設定
- 舊版本的產生工具
- systemd service 檔案
- 測試和部署文檔

**核心理念**：簡單可靠 > 複雜自動化
