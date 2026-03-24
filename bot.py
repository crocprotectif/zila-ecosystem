from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8716404969:AAE6-sLv5-Rm12-Y_w3WWaLCoYYI-pIh8ks"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("START MASUK")
    await update.message.reply_text("Bot hidup 🚀")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("RUNNING...")
app.run_polling()
