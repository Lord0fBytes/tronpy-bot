import discord
from discord.ext import commands
import json
import re
from datetime import datetime

data = ''

with open('updates.json') as json_file:
    data = json.load(json_file)

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self,ctx):
        '''
        Bot status checker
        '''
        await self.client.say("Pong!")

def setup(client):
    client.add_cog(Admin(client))