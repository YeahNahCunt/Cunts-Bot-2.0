import discord
from discord.ext import commands

client = discord.Client()

class Test_room(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Test Room is in use')
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        await channel.send(f'test {reaction.emoji} from : {reaction.message.content}')
        
        
def setup(client):
    client.add_cog(Test_room(client))
