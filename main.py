from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler

TOKEN = "8485925922:AAFM9EcljRLHF_1MxlFBm24SXrC2zko0DUc"
PHOTO_URL = "https://TUO_LINK_IMMAGINE.jpg"
TEXT = (
    "Ciaooo 😘\n\n"
    "La tua richiesta è stata approvata!\n\n"
    "🎁 Clicca qui per il regalo:\n"
    "👉 https://TUO_LINK_ESTERNO.com"
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
