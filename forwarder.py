# forwarder.py（增强版：支持群聊与媒体）
from telebot import TeleBot, types
from config import BOT_TOKEN, SOURCE_CHAT_ID, TARGET_CHAT_ID, FILTER_KEYWORDS, REPLACE_RULES
from filters import filter_message

bot = TeleBot(BOT_TOKEN)

def process_and_send_text(message):
    text = message.text or message.caption
    filtered = filter_message(text, FILTER_KEYWORDS, REPLACE_RULES)
    if filtered:
        bot.send_message(TARGET_CHAT_ID, filtered)

@bot.channel_post_handler(func=lambda m: True)
def forward_from_channel(message: types.Message):
    if message.content_type == "text":
        process_and_send_text(message)
    else:
        bot.copy_message(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

@bot.message_handler(content_types=["text", "photo", "video", "document", "audio", "voice", "sticker"])
def forward_from_group(message: types.Message):
    if message.chat and message.chat.id == SOURCE_CHAT_ID:
        if message.content_type == "text":
            process_and_send_text(message)
        else:
            bot.copy_message(
                chat_id=TARGET_CHAT_ID,
                from_chat_id=message.chat.id,
                message_id=message.message_id
            )

def run():
    print("🤖 小波波机器人已启动...")
    bot.infinity_polling()
