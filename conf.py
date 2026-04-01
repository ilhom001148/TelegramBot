import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from groq import Groq  # YANGI KUTUBXONA

load_dotenv()

# Kalitlar
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq mijozini sozlash
client = Groq(api_key=GROQ_API_KEY)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! Men Groq (Llama-3) asosida ishlaydigan botman. Savol bering!")


@dp.message()
async def chat_handler(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")

    try:
        # Groq (Llama 3) modeliga so'rov yuborish
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            model="llama-3.3-70b-versatile",  # Eng kuchli bepul model
        )

        response_text = chat_completion.choices[0].message.content
        await message.reply(response_text)

    except Exception as e:
        await message.reply(f"Xatolik yuz berdi: {e}")


async def main():
    print("🚀 Bot (Groq bilan) ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())