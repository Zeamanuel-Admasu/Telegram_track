import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Your bot token from BotFather
BOT_TOKEN = "7712509822:AAFfFaPH4vLFjKJbuCNoRGHh3J58Xb1Nhrg"

# Initialize the bot application
app = Application.builder().token(BOT_TOKEN).build()

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your python-telegram-bot 🤖")

# Add the command handler
app.add_handler(CommandHandler("start", start))

# Run the bot
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run_polling()
