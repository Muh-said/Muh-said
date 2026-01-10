import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from googletrans import Translator

# ====== TOKEN ======
TOKEN = "7989957596:AAFCj_WGugeVeNteRtO58f7-1INy1qtgY6I"
bot = telebot.TeleBot(TOKEN)

translator = Translator()

# foydalanuvchi tanlagan tilni saqlash
user_lang = {}

# ====== TIL TUGMALARI ======
def til_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton("🇺🇿 Uzbek"),
        KeyboardButton("🇬🇧 English"),
        KeyboardButton("🇷🇺 Русский"),
        KeyboardButton("🔤 Lotin → Кирилл")
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
   "🔤 Lotin → Кирилл"
])
def choose_lang(message):
    chat_id = message.chat.id

    if message.text == "🇺🇿 Uzbek":
        user_lang[chat_id] = "uz"
    elif message.text == "🇷🇺 Русский":
        user_lang[chat_id] = "ru"
    elif message.text == "🇬🇧 English":
        user_lang[chat_id] = "en"
    elif message.text == "🔤 Lotin → Кирилл":
        user_lang[chat_id] = "ru"  # lotin→kirill rus alifbosi

    bot.send_message(chat_id, "Endi matn yoz ✍️")

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
        result = translator.translate(text, dest=lang)
        bot.send_message(chat_id, result.text)
    except Exception as e:
        bot.send_message(chat_id, "Xatolik bo‘ldi ⚠️")

# ====== RUN ======
print("Bot ishga tushdi...")
bot.infinity_polling()
