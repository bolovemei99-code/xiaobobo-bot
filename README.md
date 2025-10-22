# 小波波 (@WSXBB_Bot)

俏皮语气版云端 Telegram 助手。

## 功能
- 每日报告（自动生成+发送）
- AI 聊天 (/ask)
- 群转发（可自定义）
- 云端运行 (Render)

## 部署
1. 上传全部文件到 GitHub 仓库。
2. Render → New → Background Worker。
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `python main.py`
5. 设置环境变量：
   - TELEGRAM_BOT_TOKEN：你的机器人 Token
   - ADMIN_USER_IDS：你的 Telegram 数字 ID
   - REPORT_TARGET_CHAT_ID：日报发送目标群 ID（负号开头）
   - OPENAI_API_KEY（可选）
