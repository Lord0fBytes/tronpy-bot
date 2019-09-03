import discord
from discord.ext import commands
import re
import random

class Gaming(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def show_gamers(self, ctx):
        '''
        Shows current gamers/games
        '''
        await ctx.send(":construction: I'm sorry that command is under contruction right now :construction: ")

    @commands.command()
    async def dice(self, ctx,roll):
        '''
        Rolls dice in XdX format
        '''
        pattern = re.compile('[0-9]d[0-9]{1,2}')
        if(pattern.match(roll)):
            #Rolls the dice
            roll = roll.split('d')
            results = []
            for x in range(0,int(roll[0])):
                results.append(random.randint(1,int(roll[1])+1))
            await ctx.send(results)
        else:
            await ctx.send("Invalid format: Use XdX format (ie: 1d4 or 2d20")

def setup(client):
    client.add_cog(Gaming(client))