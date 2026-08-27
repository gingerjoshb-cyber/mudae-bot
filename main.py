import os
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your actual Discord channel ID where you want the bot to roll
CHANNEL_ID = 1526629132191137792  

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    auto_roll.start()

@tasks.loop(minutes=120)  # Matches your --rr 120 timing
async def auto_roll():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("$wa")
        print("Sent automated roll command!")

@auto_roll.before_loop
async def before_auto_roll():
    await bot.wait_until_ready()

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
