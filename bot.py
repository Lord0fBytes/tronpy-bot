import discord
import json

with open('auth.json') as json_file:
    data = json.load(json_file)
    token = data['token']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # dont respond to ourselves
        if message.author == self.user:
            return
        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(token)
