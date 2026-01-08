import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from googletrans import Translator

# ====== TOKEN ======
TOKEN = "7989957596:AAFCj_WGugeVeNteRtO58f7-1INy1qtgY6I"
bot = telebot.TeleBot(TOKEN)

translator = Translator()

# foydalanuvchi tanlagan til
user_lang = {}

# ====== TIL TUGMALARI (UZ → ENG → RUS → KIRIL-LOTIN) ======
def til_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("🇺🇿 Uzbek"),
        KeyboardButton("🇬🇧 English"),
        KeyboardButton("🇷🇺 Русский")
    )
    kb.row(
        KeyboardButton("🔤 Кирилл → Lotin")
    )
    return kb

# ====== START ======
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Tilni tanla 👇",
        reply_markup=til_keyboard()
    )

# ====== TIL TANLASH ======
@bot.message_handler(func=lambda msg: msg.text in [
    "🇺🇿 Uzbek",
    "🇬🇧 English",
    "🇷🇺 Русский",
    "🔤 Кирилл → Lotin"
])
def choose_lang(message):
    chat_id = message.chat.id

    if message.text == "🇺🇿 Uzbek":
        user_lang[chat_id] = "uz"

    elif message.text == "🇬🇧 English":
        user_lang[chat_id] = "en"

    elif message.text == "🇷🇺 Русский":
        user_lang[chat_id] = "ru"

    elif message.text == "🔤 Кирилл → Lotin":
        user_lang[chat_id] = "uz"
        bot.send_message(chat_id, "Kirilcha matn yoz ✍️")
        return

    bot.send_message(chat_id, "Endi matn kiriting ✍️")

# ====== TARJIMA ======
@bot.message_handler(func=lambda msg: True)
def translate_text(message):
    chat_id = message.chat.id
    text = message.text

    if chat_id not in user_lang:
        bot.send_message(chat_id, "Avval tilni tanla ❗")
        return

    try:
        lang = user_lang[chat_id]
        result = translator.translate(text, src='auto', dest=lang)
        bot.send_message(chat_id, result.text)
    except Exception:
        bot.send_message(chat_id, "Xatolik bo‘ldi ⚠️")

# ====== RUN ======
print("Bot ishga tushdi...")
bot.infinity_polling()
