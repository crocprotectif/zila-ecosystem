from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from database import init_db,get_user,set_pin
from wallet import create_wallet
from trading import send_matic
from sniper import buy
import config

init_db()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user.id
    user = get_user(u)

    if user:
        await update.message.reply_text(f"Wallet:\n{user[1]}")
    else:
        addr = create_wallet(u)
        await update.message.reply_text(f"Wallet dibuat:\n{addr}\n/setpin 1234")

async def setpin(update: Update, context):
    set_pin(update.effective_user.id, context.args[0])
    await update.message.reply_text("PIN OK")

async def withdraw(update: Update, context):
    u = update.effective_user.id
    user = get_user(u)

    amt = float(context.args[0])
    to = context.args[1]
    pin = context.args[2]

    if user[3] != pin:
        await update.message.reply_text("PIN salah")
        return

    tx = send_matic(user,to,amt)
    await update.message.reply_text(f"TX:\n{tx}")

async def sniper(update: Update, context):
    user = get_user(update.effective_user.id)
    tx = buy(user, config.ZILA_TOKEN, 0.1)
    await update.message.reply_text(f"SNIPER:\n{tx}")

app = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("setpin",setpin))
app.add_handler(CommandHandler("withdraw",withdraw))
app.add_handler(CommandHandler("sniper",sniper))

app.run_polling()
