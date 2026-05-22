from flask import Flask, send_from_directory
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    Update
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

import threading

TOKEN = "8977162210:AAEDcvv5UUvY9FLB7YXg4kyyYB7vkPAS5Es"

# ======================
# FLASK WEB SERVER
# ======================

app_flask = Flask(__name__)

@app_flask.route("/")
def home():
    return send_from_directory(".", "index.html")

@app_flask.route("/style.css")
def style():
    return send_from_directory(".", "style.css")

@app_flask.route("/script.js")
def script():
    return send_from_directory(".", "script.js")


# ======================
# TELEGRAM BOT
# ======================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🎰 OPEN CASINO",
                web_app=WebAppInfo(
                    url="https://casino-bot-08rv.onrender.com"
                )
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎰 Welcome to Telegram Casino",
        reply_markup=reply_markup
    )


def run_flask():
    app_flask.run(host="0.0.0.0", port=5000)


telegram_app = ApplicationBuilder().token(TOKEN).build()

telegram_app.add_handler(
    CommandHandler("start", start)
)

threading.Thread(target=run_flask).start()

print("Casino Bot Running...")

telegram_app.run_polling()
