import discord
import openai
from discord.ext import commands

openai.api_key = "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"
DISCORD_BOT_TOKEN = "MTM0NzY4NDMxMzkyMzE5MDg0NA.GDNXm4.BfwPY4ze7q7MTlfQJarZoZ209ULj0Z4VvBW3-U"

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