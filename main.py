import os, json, logging
from datetime import datetime
import pytz
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
log = logging.getLogger("xiaobobo")

CONFIG_PATH = "data/config.json"
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)
else:
    cfg = {"bot_name":"小波波","bot_username":"@WSXBB_Bot","timezone":"Asia/Phnom_Penh","report_time":"09:00"}

BOT_NAME = cfg.get("bot_name")
TIMEZONE = pytz.timezone(cfg.get("timezone"))

def build_report():
    now = datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M")
    return f"🌈 嘿，这里是{BOT_NAME}的小报告～\\n🕒 时间：{now}\\n———\\n📈 今日状态：元气满满！💪\\n🧩 提醒：保持微笑，继续加油哦～😄"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"嗨！我是{BOT_NAME} 🤖\\n输入 /report 看今天的小报告吧～")

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(build_report())

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = " ".join(context.args) if context.args else ""
    if not q:
        return await update.message.reply_text("要问啥呀？比如 /ask 今天吃什么？😋")
    await update.message.reply_text(f"你问的是：{q}\\n{BOT_NAME}现在还没连上AI接口，不过我猜你想听：吃好喝好最重要～😂")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text:
        await update.message.reply_text(f"你说「{text}」，{BOT_NAME}记住啦～😉")

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("请先设置 TELEGRAM_BOT_TOKEN 环境变量")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("report", report))
    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    log.info(f"{BOT_NAME} 已启动")
    app.run_polling()

if __name__ == "__main__":
    main()
