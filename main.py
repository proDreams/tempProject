import asyncio
import os

from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

async def send_message(message: Message) -> None:
    await message.answer(text="Hello World!")

async def send_sticker(message: Message) -> None:
    await message.answer_sticker(sticker="CAACAgIAAxkBAAEKbW1lGVW1I6zFVLyovwo2rSgIt1l35QADJQACYp0ISWYMy8-mubjIMAQ")

async def start():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()

    dp.message.register(send_sticker, Command(commands="test"))
    dp.message.register(send_message)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
