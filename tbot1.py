from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8646597177:AAEwMn82f00-S6KqxSjO-P07sokuLAUwSDM"

# عند /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact_button = KeyboardButton("مرحبا بك في بوت طلب تذاكر الطيران", request_contact=True)
    keyboard = [[contact_button]]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "من فضلك اضغط على الزر لإرسال رقم هاتفك",
        reply_markup=reply_markup
    )

# استقبال رقم الهاتف
async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    phone = contact.phone_number
    name = contact.first_name

    await update.message.reply_text(f"شكراً {name}\nرقمك هو: {phone}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.CONTACT, contact_handler))

app.run_polling()