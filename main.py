import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

description = "Testing"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    """Called when bot is logged in."""
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command()
async def add(ctx: commands.Context, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(str(left + right))

load_dotenv()
token = os.getenv("TOKEN")
bot.run(token)