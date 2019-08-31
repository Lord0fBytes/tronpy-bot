import discord
from discord.ext import commands
import json
import re
from datetime import datetime

data = ''

with open('configs/updates.json') as json_file:
    data = json.load(json_file)

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self,ctx):
        '''
        Bot status checker
        '''
        await self.client.say("Pong!")

    @commands.command()
    async def hello(self, ctx):
        '''
        Greets the author
        '''
        await ctx.send("Hello! How are you? For a list of my commands type _>tb help_")

    @commands.command()
    async def show_update(self, ctx, version='0'):
        '''
        Shows the bots latest update
        '''
        pattern = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
        if version == '0':
            #Get the latest update and store it
            version = data['updates'][0]['version']
        if pattern.match(version) is not None:
            #Create and send the embed
            for update in data['updates']:
                if update['version'] == version:
                    titleField = "**`{}`\t|\t{}**".format(update['version'],update['title'])
                    typeField = "{}".format(update['type'])
                    embed=discord.Embed(title=titleField, description=update['description'], color=0xff0080)
                    embed.add_field(name="Version", value=update['version'], inline=True)
                    embed.add_field(name="Version Type", value=typeField, inline=False)
                    embed.set_footer(text="Update provided by WbPyBot | {}".format(datetime.date(datetime.now())))
                    await ctx.send(embed=embed)
                    return
            await ctx.send("Could not find that version.  #error#")
        else:
            await ctx.send('Invalid version format \{X.Y.Z\}   #error#')

    @commands.command()
    async def show_history(self,ctx,limit=10):
        '''
        Shows the history of updates
        '''
        historyTitle = '__Available History:__\n'
        historyText = ""
        # Prechecks to the arguments; need to be number, >0, and less than the number of updates
        if not isinstance(limit,int):
            await ctx.send("Invaild `limit` format (number only)  #error#")
            return
        if limit < 1:
            await ctx.send("Number cannot be <= 0  #error#")
            return
        if limit > len(data['updates']):
            limit = len(data['updates'])
        #Loop through limit values
        for i in range(0,limit):
            #define data value (clean purposes)
            update = data['updates'][i]
            historyText += "`{}` | {} (_{}_)\n".format(update['version'],update['title'],update['timestamp'])
        #Create embed text
        embed=discord.Embed(title=historyTitle, description=historyText, color=0xff0080)
        embed.set_footer(text="Update provided by WbPyBot | {}".format(datetime.date(datetime.now())))
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Utilities(client))