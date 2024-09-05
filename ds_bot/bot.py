import asyncio
import os
import ssl
import certifi
from discord import Intents
import discord
from dotenv import load_dotenv
from tg_bot.bot import to_tg

load_dotenv()

DS_KEY = os.getenv("DS_KEY")
ssl_context = ssl.create_default_context(cafile=certifi.where())

intents = Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Bot is connected to server")


@client.event
async def on_message(message):
    print(f'{message.author} - {message.content}')
    if "update" in message.content.lower():
        await asyncio.run(to_tg(message.content))


client.run(DS_KEY)

