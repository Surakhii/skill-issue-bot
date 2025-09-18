import os
import random
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TENOR_KEY = os.getenv("TENOR_KEY")

# Discord intents (we need guilds for channel creation)
intents = discord.Intents.default()
intents.guilds = True  # needed for on_guild_channel_create

bot = commands.Bot(command_prefix="!", intents=intents)

# Function to fetch a random "skill issue" GIF from Tenor
def get_skill_issue_gif():
    url = f"https://g.tenor.com/v1/search?q=skill%20issue&key={TENOR_KEY}&limit=50"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Pick a random GIF URL
            gif_url = random.choice(data["results"])["media"][0]["gif"]["url"]
            return gif_url
    except Exception as e:
        print(f"Error fetching GIF: {e}")
    return None

# Bot ready event
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Detect when a new text channel is created
@bot.event
async def on_guild_channel_create(channel):
    # Only respond to text channels, and names starting with ticket-
    if isinstance(channel, discord.TextChannel) and channel.name.startswith("ticket-"):
        gif_url = get_skill_issue_gif()
        if gif_url:
            await channel.send(gif_url)
        else:
            await channel.send("Couldn't fetch a skill issue GIF 😅")

# Run the bot
bot.run(TOKEN)
