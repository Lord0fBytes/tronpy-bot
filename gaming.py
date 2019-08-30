import discord
from discord.ext import commands

class Gaming(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def show_gamers(ctx):
        '''
        Shows current gamers/games
        '''
        await ctx.send(":construction: I'm sorry that command is under contruction right now :construction: ")

def setup(client):
    client.add_cog(Gaming(client))