import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler

TOKEN = os.environ.get("BOT_TOKEN")
PHOTO_URL = "https://instasize.com/p/1f0e2543b0c113c2d9912fed813c305807a68070553664a7fb913597a70e6a4a"
TEXT = (
    "Ciaooo 😘\n\n"
    "La tua richiesta è stata approvata!\n\n"
    "🎁 Clicca qui per il tuo regalo: è gratis!\n"
    "👉https://onlyfans.com/sofiaitalia2006/c47"
)

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat_id = update.chat_join_request.chat.id

    await context.bot.approve_chat_join_request(chat_id, user.id)

    try:
        await context.bot.send_photo(
            chat_id=user.id,
            photo=PHOTO_URL,
            caption=TEXT
        )
    except:
        pass

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(handle_join_request))
app.run_polling()
