import discord
from discord.ext import commands
from datetime import datetime, time
import sys
import os


# Config.py setup
if not os.path.isfile("config.py"):
    sys.exit("'config.py' tidak ditemukan!")
else:
    import config


TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=config.prefik, intents=intents, description=config.deskripsi)


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}({client.user.id})")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="VTUBERS"))
    print("Bot is online")
    
@client.command()
async def ping(ctx):
    """ Ping bot! """
    try:
        start = time.perf_counter()
        message = await ctx.send("Eh...")
        end = time.perf_counter()
        ping = (end - start) * 1000
        latency = client.latency * 1000
        print(f"Ada yang ngeping bot! Latensi/Response : {round(latency)}/{round(ping,2)} ms")
        embed = discord.embed(title="PING PONG!", description=f"**Latency**: {round(latency)}ms\n**Response time**: {round(ping,2)}ms", color=0xff6a3d)
        await message.edit(content=f"Oh... **Pong!**", embed = embed)
    except:
        await ctx.send(config.err_msg_gtw)

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    """ Menjalankan ekstensi """
    client.load_extension(f"bot.cogs.{extension}")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    """ Mencopot ekstensi """
    client.unload_extension(f"bot.cogs.{extension}")

for filename in os.listdir(f"bot/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"bot.cogs.{filename[:-3]}")

if __name__ == "__main__":
    client.run(TOKEN)
