import discord
import openai
from discord.ext import commands

import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

print(f"OpenAI API Key: {OPENAI_API_KEY}")
print(f"Discord Bot Token: {DISCORD_BOT_TOKEN}")

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

faq = {
    "how do I become funded by Summit Strike Cap": "In order to trade a funded account...",
    "how many accounts can I trade": "You can purchase and trade multiple evaluation accounts...",
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  

    user_question = message.content.lower()

    for question, answer in faq.items():
        if question in user_question:
            await message.channel.send(answer)
            return  

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_question}]
    )

    reply = response["choices"][0]["message"]["content"]
    await message.channel.send(reply)

bot.run(DISCORD_BOT_TOKEN)