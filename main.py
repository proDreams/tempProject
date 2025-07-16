import asyncio
import os

from aiogram import Dispatcher, Bot
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

async def send_message(message: Message) -> None:
    await message.answer(text="Hello World!")

async def start():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()

    dp.message.register(send_message)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
