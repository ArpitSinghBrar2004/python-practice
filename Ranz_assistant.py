import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
Token = os.getenv("Discord_Token")

intents= discord.Intents.default()
intents.message_content=True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is online !")
@bot.event
async def on_message(msg):
    if msg.author.id != bot.user.id:
        await msg.channel.send(f"Interesting message ,{msg.author.mention} ")
@bot.tree.command(name="greet",description="sends a greeting to user ")
async def greet (interaction: discord.Interaction):
    username=interaction.user.mention
    await interaction.response.send_message(f"Hello there ,{username}")

bot.run(Token)