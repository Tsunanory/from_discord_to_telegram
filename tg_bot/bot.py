import os
import aiogram
from dotenv import load_dotenv
import asyncio

load_dotenv()

TG_KEY = os.getenv("TG_KEY")
chat_id = 147769504

bot = aiogram.Bot(token=TG_KEY)
aiogram.Dispatcher()


async def handle(text):
    await bot.send_message(chat_id, text)


async def to_tg(message):
    await handle(message)

