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
    if "update" in message.content.lower():
        await to_tg(f'Канал: {message.channel.name.capitalize()}\n'
                    f'Сообщение: {message.content[0:40] if len(message.content) > 40 else message.content}\n'
                    f'Ссылка: https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}')


client.run(DS_KEY)

# https://discord.com/channels/{guild=Guild id}/{TextChannel id}/{message id}