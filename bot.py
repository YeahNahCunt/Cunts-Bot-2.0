import discord
from discord.ext import commands

lient = commands.Bot(command_prefix = '|') #holder prefix change later

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


client.run(os.environ['BOT_TOKEN'])
