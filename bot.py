import discord
from discord.ext import commands
import json

with open('auth.json') as json_file:
    data = json.load(json_file)
    token = data['token']
with open('config.json') as config_file:
    data = json.load(config_file)
    prefix = data['prefix']

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send("%s says Hello, World!" % (ctx.author))

bot.run(token)


