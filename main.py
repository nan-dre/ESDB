import os
import random

from discord.ext import commands
from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
STREAM = r'http://jazz-wr04.ice.infomaniak.ch/jazz-wr04-128.mp3'


bot = commands.Bot(command_prefix='/')

@bot.command()
async def swing(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    source = await discord.FFmpegOpusAudio.from_probe(STREAM, method='fallback')
    vc.play(source)
    

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(TOKEN)
