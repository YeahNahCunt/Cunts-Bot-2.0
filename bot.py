import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '|') #holder prefix change later

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Suck ya mum'))
    print('Bot is ready!')
    print(discord.__version__)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('*******************')

##testing if online##
@client.command()
async def ping(ctx):
    await ctx.send(f'Surprise motherfucker in {client.latency * 1000}ms')
    
    
    
    
    
    
    
    
##Load Cogs##
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'I have loaded the {extension} and is now usable')

##UNLoad Cogs##
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'I have unloaded the {extension} and is now inoperable')

##RELoad Cogs##
@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'I have reloaded the {extension} and is now usable')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

        
client.run(os.environ['BOT_TOKEN'])
