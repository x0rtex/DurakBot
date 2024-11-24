import os

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD")

MY_GUILD = discord.Object(id=GUILD)


class MyClient(discord.Client):
    def __init__(self, *, client_intents: discord.Intents):
        super().__init__(intents=client_intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(client_intents=intents)

@client.event
async def on_ready():
    """Called when bot is logged in."""
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")

# noinspection PyUnresolvedReferences
@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')


# noinspection PyUnresolvedReferences
@client.tree.command()
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')

client.run(TOKEN)