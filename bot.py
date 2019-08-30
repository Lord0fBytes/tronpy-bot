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

extensions = ['utilities','gaming','stream']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension,error))
    bot.run(token)


