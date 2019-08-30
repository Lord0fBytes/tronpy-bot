import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self):
        '''
        Bot status checker
        '''
        await self.client.say("Pong!")

    @commands.command()
    async def hello(ctx):
        '''
        Greets the author
        '''
        await ctx.send("Hello! How are you? For a list of my commands type _>tb help_")

    @commands.command()
    async def show_update(ctx):
        '''
        Shows the bots latest update
        '''
        await ctx.send(":construction: I'm sorry that command is under contruction right now :construction: ")


def setup(client):
    client.add_cog(Utilities(client))