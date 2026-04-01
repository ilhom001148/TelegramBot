# import os
# import asyncio
# from dotenv import load_dotenv
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from groq import Groq
#
# load_dotenv()
#
# TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
#
# client = Groq(api_key=GROQ_API_KEY)
#
# bot = Bot(token=TELEGRAM_TOKEN)
# dp = Dispatcher()
#
#
# @dp.message(Command("start"))
# async def start(message: types.Message):
#     await message.answer("Salom! Men Groq (Llama-3) asosida ishlaydigan botman. Savol bering!")
#
#
# @dp.message()
# async def chat_handler(message: types.Message):
#     await bot.send_chat_action(message.chat.id, "typing")
#
#     try:
#         chat_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": message.text}],
#             model="llama-3.3-70b-versatile",  # Eng kuchli bepul model
#         )
#
#         response_text = chat_completion.choices[0].message.content
#         await message.reply(response_text)
#
#     except Exception as e:
#         await message.reply(f"Xatolik yuz berdi: {e}")
#
#
# async def main():
#     print("🚀 Bot (Groq bilan) ishga tushdi...")
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())



#
# import os
# import asyncio
# from dotenv import load_dotenv
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from groq import Groq
#
# load_dotenv()
#
# TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
#
# client = Groq(api_key=GROQ_API_KEY)
#
# bot = Bot(token=TELEGRAM_TOKEN)
# dp = Dispatcher()
#
#
# @dp.message(Command("start"))
# async def start(message: types.Message):
#     await message.answer("Salom! Men dasturlash o‘qituvchi AI botman. Python, Java, C, C++, Go haqida savol bering!")
#
#
# @dp.message()
# async def chat_handler(message: types.Message):
#     await bot.send_chat_action(message.chat.id, "typing")
#
#     try:
#         chat_completion = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": """
# Sen professional dasturlash o‘qituvchisisan.
#
# Mavzular:
# - Python
# - Java
# - C
# - C++
# - Go
# - va boshqa dasturlash tillari
#
# Qoidalar:
# - Har doim aniq va tushunarli javob ber
# - Agar foydalanuvchi kod so‘rasa → to‘liq ishlaydigan kod yoz
# - Kodni alohida blokda yoz
# - Kodni oddiy va tushunarli qilib tushuntir
# - Beginner uchun ham tushunarli bo‘lsin
# - Kerak bo‘lsa misol keltir
# """
#                 },
#                 {
#                     "role": "user",
#                     "content": message.text
#                 }
#             ]
#         )
#
#         response_text = chat_completion.choices[0].message.content
#         await message.reply(response_text)
#
#     except Exception as e:
#         await message.reply(f"Xatolik yuz berdi: {e}")
#
#
# async def main():
#     print("🚀 Bot (Groq + Coding AI) ishga tushdi...")
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

#
#
# import os
# import asyncio
# from dotenv import load_dotenv
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from groq import Groq
#
# load_dotenv()
#
# TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
#
# client = Groq(api_key=GROQ_API_KEY)
#
# bot = Bot(token=TELEGRAM_TOKEN)
# dp = Dispatcher()
#
#
# @dp.message(Command("start"))
# async def start(message: types.Message):
#     await message.answer(
#         "Salom! Men faqat dasturlash bo‘yicha javob beraman.\n"
#         "Python, Java, C, C++, Go haqida savol bering!"
#     )
#
#
# @dp.message()
# async def chat_handler(message: types.Message):
#     await bot.send_chat_action(message.chat.id, "typing")
#
#     try:
#         chat_completion = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": """
# Sen faqat dasturlash bo‘yicha javob beradigan AI botsan.
#
# RUXSAT ETILGAN MAVZULAR:
# - Python
# - Java
# - C
# - C++
# - Go
# - Algoritmlar va dasturlash
#
# QOIDALAR:
# - Agar savol dasturlashga tegishli bo‘lmasa:
#   → "Kechirasiz, men faqat dasturlash savollariga javob beraman" deb yoz
# - Hech qachon boshqa mavzularga javob bermagin
# - Agar savol dasturlashga tegishli bo‘lsa:
#   → to‘liq, tushunarli va aniq javob ber
#   → kerak bo‘lsa kod yoz
#   → kodni alohida blokda yoz
#   → tushuntirib ber
# """
#                 },
#                 {
#                     "role": "user",
#                     "content": message.text
#                 }
#             ]
#         )
#
#         response_text = chat_completion.choices[0].message.content
#         await message.reply(response_text)
#
#     except Exception as e:
#         await message.reply(f"Xatolik yuz berdi: {e}")
#
#
# async def main():
#     print("🚀 Bot (Strict Coding AI) ishga tushdi...")
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
#

#
#
# import os
# import asyncio
# from dotenv import load_dotenv
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from groq import Groq
#
# load_dotenv()
#
# # ================= CONFIG =================
# TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# ADMIN_ID = int(os.getenv("ADMIN_ID"))
#
# client = Groq(api_key=GROQ_API_KEY)
#
# bot = Bot(token=TELEGRAM_TOKEN)
# dp = Dispatcher()
#
# # ================= DATA =================
# user_lang = {}
# users = set()
# reports = []
#
# # ================= PROMPT =================
# def get_prompt(lang):
#     return f"""
# Sen faqat dasturlash bo‘yicha javob beradigan AI botsan.
#
# Javob tili: {lang}
#
# QOIDALAR:
# - Agar savol dasturlashga tegishli bo‘lmasa:
#   → "Kechirasiz, men faqat dasturlash savollariga javob beraman"
# - Agar savol dasturlashga tegishli bo‘lsa:
#   → aniq, to‘liq javob ber
#   → kerak bo‘lsa kod yoz
#   → tushuntir
# """
#
# # ================= START =================
# @dp.message(Command("start"))
# async def start(message: types.Message):
#     user_lang[message.from_user.id] = "uzbek"
#     users.add(message.from_user.id)
#
#     await message.answer(
#         "🚀 Salom!\n\n"
#         "Tilni tanlang:\n"
#         "1 - Uzbek\n"
#         "2 - English\n"
#         "3 - Russian"
#     )
#
# # ================= LANGUAGE =================
# @dp.message(lambda message: message.text in ["1", "2", "3"])
# async def set_lang(message: types.Message):
#     user_id = message.from_user.id
#
#     if message.text == "1":
#         user_lang[user_id] = "uzbek"
#         await message.answer("🇺🇿 Uzbek tanlandi")
#     elif message.text == "2":
#         user_lang[user_id] = "english"
#         await message.answer("🇬🇧 English selected")
#     elif message.text == "3":
#         user_lang[user_id] = "russian"
#         await message.answer("🇷🇺 Русский выбран")
#
# # ================= REPORT =================
# @dp.message(Command("report"))
# async def report(message: types.Message):
#     text = message.text.replace("/report", "").strip()
#
#     report_data = {
#         "user": message.from_user.full_name,
#         "id": message.from_user.id,
#         "text": text
#     }
#
#     reports.append(report_data)
#
#     # ADMIN ga yuborish
#     await bot.send_message(
#         ADMIN_ID,
#         f"🚨 SHIKOYAT:\n\n"
#         f"User: {message.from_user.full_name}\n"
#         f"ID: {message.from_user.id}\n\n"
#         f"Matn: {text}"
#     )
#
#     await message.answer("Shikoyatingiz qabul qilindi ✅")
#
# # ================= ADMIN PANEL =================
# @dp.message(Command("admin"))
# async def admin_panel(message: types.Message):
#     if message.from_user.id != ADMIN_ID:
#         return await message.answer("❌ Ruxsat yo‘q")
#
#     await message.answer(
#         "🛠 Admin Panel:\n"
#         "/stats - statistika\n"
#         "/users - userlar\n"
#         "/reports - shikoyatlar\n"
#     )
#
# # ================= STATS =================
# @dp.message(Command("stats"))
# async def stats(message: types.Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#
#     await message.answer(
#         f"📊 Statistika:\n\n"
#         f"👥 Userlar: {len(users)}\n"
#         f"🚨 Shikoyatlar: {len(reports)}"
#     )
#
# # ================= USERS =================
# @dp.message(Command("users"))
# async def show_users(message: types.Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#
#     await message.answer(f"👥 Userlar soni: {len(users)}")
#
# # ================= REPORTS =================
# @dp.message(Command("reports"))
# async def show_reports(message: types.Message):
#     if message.from_user.id != ADMIN_ID:
#         return
#
#     if not reports:
#         return await message.answer("Hech qanday shikoyat yo‘q")
#
#     text = "🚨 SHIKOYATLAR:\n\n"
#
#     for r in reports[-10:]:
#         text += f"{r['id']} - {r['text']}\n"
#
#     await message.answer(text)
#
# # ================= LOG + AI =================
# @dp.message(lambda message: message.text)
# async def handle_text(message: types.Message):
#     user_id = message.from_user.id
#     users.add(user_id)
#
#     # 👉 ADMIN LOG
#     await bot.send_message(
#         ADMIN_ID,
#         f"📩 Xabar:\n\n"
#         f"👤 {message.from_user.full_name}\n"
#         f"🆔 {user_id}\n"
#         f"💬 {message.text}"
#     )
#
#     lang = user_lang.get(user_id, "uzbek")
#
#     await bot.send_chat_action(message.chat.id, "typing")
#
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[
#             {"role": "system", "content": get_prompt(lang)},
#             {"role": "user", "content": message.text}
#         ]
#     )
#
#     await message.answer(response.choices[0].message.content)
#
# # ================= MAIN =================
# async def main():
#     print("🚀 Full Pro Bot ishga tushdi")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())




import os
import asyncio
import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from groq import Groq

load_dotenv()

# ================= CONFIG =================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

client = Groq(api_key=GROQ_API_KEY)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# ================= DATA =================
user_lang = {}
users = set()
reports = []

# ================= PROMPT =================
def get_prompt(lang):
    return f"""
Sen faqat dasturlash bo‘yicha javob beradigan AI botsan.

Javob tili: {lang}

QOIDALAR:
- Agar savol dasturlashga tegishli bo‘lmasa:
  → "Kechirasiz, men faqat dasturlash savollariga javob beraman"
- Agar savol dasturlashga tegishli bo‘lsa:
  → aniq, to‘liq javob ber
  → kerak bo‘lsa kod yoz
  → tushuntir
"""

# ================= START =================
@dp.message(Command("start"))
async def start(message: types.Message):
    user_lang[message.from_user.id] = "uzbek"
    users.add(message.from_user.id)

    await message.answer(
        "🚀 Salom!\n\n"
        "Tilni tanlang:\n"
        "1 - Uzbek\n"
        "2 - English\n"
        "3 - Russian"
    )

# ================= LANGUAGE =================
@dp.message(lambda message: message.text in ["1", "2", "3"])
async def set_lang(message: types.Message):
    user_id = message.from_user.id

    if message.text == "1":
        user_lang[user_id] = "uzbek"
        await message.answer("🇺🇿 Uzbek tanlandi")
    elif message.text == "2":
        user_lang[user_id] = "english"
        await message.answer("🇬🇧 English selected")
    elif message.text == "3":
        user_lang[user_id] = "russian"
        await message.answer("🇷🇺 Русский выбран")

# ================= REPORT =================
@dp.message(Command("report"))
async def report(message: types.Message):
    text = message.text.replace("/report", "").strip()

    report_data = {
        "user": message.from_user.full_name,
        "id": message.from_user.id,
        "text": text
    }

    reports.append(report_data)

    await bot.send_message(
        ADMIN_ID,
        f"🚨 SHIKOYAT:\n\n"
        f"User: {message.from_user.full_name}\n"
        f"ID: {message.from_user.id}\n\n"
        f"Matn: {text}"
    )

    await message.answer("Shikoyatingiz qabul qilindi ✅")

# ================= ADMIN PANEL =================
@dp.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Ruxsat yo‘q")

    await message.answer(
        "🛠 Admin Panel:\n"
        "/stats - statistika\n"
        "/users - userlar\n"
        "/reports - shikoyatlar\n"
    )

# ================= STATS =================
@dp.message(Command("stats"))
async def stats(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        f"📊 Statistika:\n\n"
        f"👥 Userlar: {len(users)}\n"
        f"🚨 Shikoyatlar: {len(reports)}"
    )

# ================= USERS =================
@dp.message(Command("users"))
async def show_users(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(f"👥 Userlar soni: {len(users)}")

# ================= REPORTS =================
@dp.message(Command("reports"))
async def show_reports(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    if not reports:
        return await message.answer("Hech qanday shikoyat yo‘q")

    text = "🚨 SHIKOYATLAR:\n\n"

    for r in reports[-10:]:
        text += f"{r['id']} - {r['text']}\n"

    await message.answer(text)

# ================= FULL LOG + AI =================
@dp.message(lambda message: message.text)
async def handle_text(message: types.Message):
    user = message.from_user
    chat = message.chat

    user_id = user.id
    users.add(user_id)

    # ===== FULL LOG =====
    log_text = (
        f"📩 YANGI XABAR\n\n"
        f"👤 Ism: {user.full_name}\n"
        f"🔗 Username: @{user.username if user.username else 'yo‘q'}\n"
        f"🆔 User ID: {user_id}\n"
        f"💬 Xabar: {message.text}\n\n"
        f"📊 Chat ID: {chat.id}\n"
        f"💬 Chat turi: {chat.type}\n"
        f"🌐 Language: {user.language_code}\n"
        f"⭐ Premium: {getattr(user, 'is_premium', False)}\n"
        f"🆔 Message ID: {message.message_id}\n"
        f"⏰ Time: {datetime.datetime.now()}\n"
    )

    # ===== EXTRA =====
    if message.reply_to_message:
        log_text += "\n↩️ Reply bor"

    if message.photo:
        log_text += "\n📷 Rasm yubordi"

    if message.video:
        log_text += "\n🎥 Video yubordi"

    if message.document:
        log_text += "\n📄 Fayl yubordi"

    # ===== ADMINGA YUBORISH =====
    await bot.send_message(ADMIN_ID, log_text)

    lang = user_lang.get(user_id, "uzbek")

    await bot.send_chat_action(chat.id, "typing")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": get_prompt(lang)},
            {"role": "user", "content": message.text}
        ]
    )

    await message.answer(response.choices[0].message.content)

# ================= MAIN =================
async def main():
    print("🚀 Full Pro Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())