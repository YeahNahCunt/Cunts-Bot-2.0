import discord
from discord.ext import commands

client = discord.Client()

class Test_room(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Test Room is in use')
        
 def setup(client):
    client.add_cog(Test_room(client))
