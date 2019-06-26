import discord
import random
import json
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from imgurpython import ImgurClient
import os

#clients or defining variables#
client = commands.Bot(command_prefix = '*')
client.remove_command('help')


#For Bot Debug and status#
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='*help'))
    print('Bot is ready.')
    print(discord.__version__)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('*******************')


@client.command()
async def ping(ctx):
    async with ctx.typing():
        await asyncio.sleep(.05)
            
        await ctx.send('Pong!')

@client.command()
async def pingNSFW(ctx):
    async with ctx.typing():
        await asyncio.sleep(.05)
    async with ctx.typing():
        await asyncio.sleep(.05)

    if  ctx.channel.is_nsfw():
        await ctx.send("Go for it you filthy animal")
    else : 
        await ctx.send("You can't use that command here idiot! GO to a NSFW room!")


# #help home#
# @client.command()
# async def help(ctx):
#     async with ctx.typing():
#         await asyncio.sleep(.05)
            
#     embed = discord.Embed(
#         description = 'Below you will find a list of help commands that you can use with me',
#         colour = discord.Colour.purple()
#     )

#     embed.set_author(name='Cunts Bot Helpcenter')
#     embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
#     embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
#     embed.add_field(name=':speech_balloon:  Translations :speech_balloon:', value= '`help_translations`', inline=False)
#     embed.add_field(name=':baby_bottle: Safe for work commands :baby_bottle:', value= '`help_sfw`', inline=False)
#     embed.add_field(name=':underage: NSFW commands :underage:', value= '`help_nsfw`', inline=False)

#     await ctx.send(embed=embed)

# #translate help
# @client.command()
# async def help_translations(ctx):
#     async with ctx.typing():
#         await asyncio.sleep(.05)
            
#     embed = discord.Embed(
#         description = 'Translation help centre instructions',
#         colour = discord.Colour.purple()
#     )

#     embed.set_author(name='Cunts Bot Helpcenter for Translations')
#     embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
#     embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
#     embed.add_field(name=':speech_balloon:  Translations :speech_balloon: ', value=
#     '`The bot can do translations for the following languages:`\n'+
#     '\u200b\n'+ #cheat for line break
#     'React to message with :flag_gb: for an ENGLISH translation\n'+
#     'React to message with :flag_sa: for an ARABIC translation\n'+
#     '\u200b\n'+
#     'If you would like any other languages added to the functionality plese contact Cunt ( Disturbed#3853 )', 
#     inline=False)
#     await ctx.send(embed=embed)

# #SFW help
# @client.command()
# async def help_sfw(ctx):
#     async with ctx.typing():
#         await asyncio.sleep(.05)
            
#     embed = discord.Embed(
#         description = 'Safe for general rooms help centre instructions',
#         colour = discord.Colour.purple()
#     )

#     embed.set_author(name='Cunts Bot Helpcenter for SFW')
#     embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
#     embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
#     embed.add_field(name=':baby_bottle: Safe for work commands :baby_bottle:', value=
#     '\u200b\n'+ #cheat for line break
#     '`iwant memes        :` For dank Memes\n'+
#     '`iwant gifs         :` For dank Gifs\n'+
#     '`iwant aww          :` For all of the cuteness\n'+
#     '`oicunt             :` Ask me questions\n'+
#     '`ship               :` Who are you compatable with?\n'+
#     '`insult             :` Mention yourself or someone else to get a sick burn\n'
#     '`howgay             :` Mention yourself or someone else to find out how gay they are\n'+
#     '`dong               :` Mention yourself or someone else to find out their dong length\n'+
#     '`islamqa            :` For the newest questions being asked on islamqa.info\n'
#     '\u200b\n' 
#      , inline=False)
#     await ctx.send(embed=embed)

# #NSFW help
# @client.command()
# async def help_nsfw(ctx):
#     if  ctx.channel.is_nsfw(): #checks if room is NSFW or not
#         async with ctx.typing():
#             await asyncio.sleep(.05)
            
#         embed = discord.Embed(
#             description = 'NSFW help centre instructions',
#             colour = discord.Colour.purple()
#         )

#         embed.set_author(name='Cunts Bot Helpcenter for NSFW')
#         embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
#         embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
#         embed.add_field(name=':underage: General NSFW :underage:', value=
#         '\u200b\n'+ #cheat for line break
#         '`nsfw amateur       :` Amateur girls\n'+
#         '`nsfw anal          :` For your anal fixations\n'+
#         '`nsfw ass           :` For some sweet booty\n'+
#         '`nsfw boobs         :` Mmmmhhh boobs\n'+
#         '`nsfw gonewild      :` random image from gonewild subreddit\n'
#         '`nsfw milf          :` Hot mommas\n'+
#         '`nsfw gifs          :` Sexy gifs\n'+
#         '`nsfw petite        :` Petite cute girls\n'+
#         '`nsfw teen          :` Legal teens\n'+
#         '\u200b' #cheat for line break
#         , inline=False)
#         embed.add_field(name=':fire: KINK NSFW :fire:', value=
#         '\u200b\n'+ #cheat for line break
#         '`nsfw blowjob       :` Sexy BJs\n'+
#         '`nsfw BDSM          :` Hot, sweaty and rough\n'+
#         '`nsfw celeb         :` Celebs and their best nude/sexy content\n'+
#         '`nsfw cum           :` We got your protein fix here\n'+
#         '`nsfw fit           :` Female Body Perfection\n'
#         '`nsfw gay           :` A place for sexy guys\n'+
#         '`nsfw lesbian       :` Girl on girl action\n'+
#         '`nsfw orgasm        :` "O" Faces. Faces of Ecstasy\n'+
#         '`nsfw outfits       :` Hot pics of people in NSFW Outfits\n'+
#         '`nsfw pussy         :` It is not about cats\n'+
#         '`nsfw thicc         :` Sexy curves\n'+
#         '`nsfw thigh         :` Thick thighs and luscious curves\n'+
#         '`nsfw trans         :` Traps and trans\n'+
#         '`nsfw hentai        :` Rule 34 an dother weeb trash\n'+
#         '\u200b' #cheat for line break
#         , inline=False)
#         embed.add_field(name=':earth_africa: Ethnic NSFW :earth_asia:', value=
#         '\u200b\n'+ #cheat for line break
#         '`nsfw ethnic        :` For your random exotic cravings\n'+
#         '`nsfw arab          :` Middle eastern hotties\n'+
#         '`nsfw asian         :` For that Eastern taste\n'+
#         '`nsfw black         :` Tastes like chocolate\n'+
#         '`nsfw latin        :` Hot blooded latin girls\n'
#         '`nsfw indian        :` Spicy indian girls\n'+
#         '`nsfw white         :` Pale cuties\n'+
#         '\u200b' #cheat for line break
#         , inline=False)
#         await ctx.send(embed=embed)

#     else : 
#             await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
#     if  ctx.channel.is_nsfw():
#         await ctx.send("Go for it you filthy animal")
#     else : 
#         await ctx.send("You can't use that command here idiot! GO to a NSFW room!")


# #help home#
# @client.command()
# async def help(ctx):
#     async with ctx.typing():
#         await asyncio.sleep(.05)
            
#     embed = discord.Embed(
#         description = 'Below you will find a list of help commands that you can use with me',
#         colour = discord.Colour.purple()
#     )

#     embed.set_author(name='Cunts Bot Helpcenter')
#     embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
#     embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
#     embed.add_field(name=':speech_balloon:  Translations :speech_balloon:', value= '`help_translations`', inline=False)
#     embed.add_field(name=':baby_bottle: Safe for work commands :baby_bottle:', value= '`help_sfw`', inline=False)
#     embed.add_field(name=':underage: NSFW commands :underage:', value= '`help_nsfw`', inline=False)

#     await ctx.send(embed=embed)

# #translate help
# @client.command()
# async def help_translations(ctx):
#     async with ctx.typing():
#         await asyncio.sleep(.05)
            
#     embed = discord.Embed(
#         description = 'Translation help centre instructions',
#         colour = discord.Colour.purple()
#     )

#     embed.set_author(name='Cunts Bot Helpcenter for Translations')
#     embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
#     embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
#     embed.add_field(name=':speech_balloon:  Translations :speech_balloon: ', value=
#     '`The bot can do translations for the following languages:`\n'+
#     '\u200b\n'+ #cheat for line break
#     'React to message with :flag_gb: for an ENGLISH translation\n'+
#     'React to message with :flag_sa: for an ARABIC translation\n'+
#     '\u200b\n'+
#     'If you would like any other languages added to the functionality plese contact Cunt ( Disturbed#3853 )', 
#     inline=False)
#     await ctx.send(embed=embed)

# #SFW help
# @client.command()
# async def help_sfw(ctx):
#     async with ctx.typing():
#         await asyncio.sleep(.05)
            
#     embed = discord.Embed(
#         description = 'Safe for general rooms help centre instructions',
#         colour = discord.Colour.purple()
#     )

#     embed.set_author(name='Cunts Bot Helpcenter for SFW')
#     embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
#     embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
#     embed.add_field(name=':baby_bottle: Safe for work commands :baby_bottle:', value=
#     '\u200b\n'+ #cheat for line break
#     '`iwant memes        :` For dank Memes\n'+
#     '`iwant gifs         :` For dank Gifs\n'+
#     '`iwant aww          :` For all of the cuteness\n'+
#     '`oicunt             :` Ask me questions\n'+
#     '`ship               :` Who are you compatable with?\n'+
#     '`insult             :` Mention yourself or someone else to get a sick burn\n'
#     '`howgay             :` Mention yourself or someone else to find out how gay they are\n'+
#     '`dong               :` Mention yourself or someone else to find out their dong length\n'+
#     '`islamqa            :` For the newest questions being asked on islamqa.info\n'
#     '\u200b\n' 
#      , inline=False)
#     await ctx.send(embed=embed)

# #NSFW help
# @client.command()
# async def help_nsfw(ctx):
#     if  ctx.channel.is_nsfw(): #checks if room is NSFW or not
#         async with ctx.typing():
#             await asyncio.sleep(.05)
            
#         embed = discord.Embed(
#             description = 'NSFW help centre instructions',
#             colour = discord.Colour.purple()
#         )

#         embed.set_author(name='Cunts Bot Helpcenter for NSFW')
#         embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
#         embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
#         embed.add_field(name=':underage: General NSFW :underage:', value=
#         '\u200b\n'+ #cheat for line break
#         '`nsfw amateur       :` Amateur girls\n'+
#         '`nsfw anal          :` For your anal fixations\n'+
#         '`nsfw ass           :` For some sweet booty\n'+
#         '`nsfw boobs         :` Mmmmhhh boobs\n'+
#         '`nsfw gonewild      :` random image from gonewild subreddit\n'
#         '`nsfw milf          :` Hot mommas\n'+
#         '`nsfw gifs          :` Sexy gifs\n'+
#         '`nsfw petite        :` Petite cute girls\n'+
#         '`nsfw teen          :` Legal teens\n'+
#         '\u200b' #cheat for line break
#         , inline=False)
#         embed.add_field(name=':fire: KINK NSFW :fire:', value=
#         '\u200b\n'+ #cheat for line break
#         '`nsfw blowjob       :` Sexy BJs\n'+
#         '`nsfw BDSM          :` Hot, sweaty and rough\n'+
#         '`nsfw celeb         :` Celebs and their best nude/sexy content\n'+
#         '`nsfw cum           :` We got your protein fix here\n'+
#         '`nsfw fit           :` Female Body Perfection\n'
#         '`nsfw gay           :` A place for sexy guys\n'+
#         '`nsfw lesbian       :` Girl on girl action\n'+
#         '`nsfw orgasm        :` "O" Faces. Faces of Ecstasy\n'+
#         '`nsfw outfits       :` Hot pics of people in NSFW Outfits\n'+
#         '`nsfw pussy         :` It is not about cats\n'+
#         '`nsfw thicc         :` Sexy curves\n'+
#         '`nsfw thigh         :` Thick thighs and luscious curves\n'+
#         '`nsfw trans         :` Traps and trans\n'+
#         '`nsfw hentai        :` Rule 34 an dother weeb trash\n'+
#         '\u200b' #cheat for line break
#         , inline=False)
#         embed.add_field(name=':earth_africa: Ethnic NSFW :earth_asia:', value=
#         '\u200b\n'+ #cheat for line break
#         '`nsfw ethnic        :` For your random exotic cravings\n'+
#         '`nsfw arab          :` Middle eastern hotties\n'+
#         '`nsfw asian         :` For that Eastern taste\n'+
#         '`nsfw black         :` Tastes like chocolate\n'+
#         '`nsfw latin        :` Hot blooded latin girls\n'
#         '`nsfw indian        :` Spicy indian girls\n'+
#         '`nsfw white         :` Pale cuties\n'+
#         '\u200b' #cheat for line break
#         , inline=False)
#         await ctx.send(embed=embed)

#     else : 
#             await ctx.send("You can't use that command here idiot! GO to a NSFW room!")



##Load Cogs##
# client.load_extension('cogs.SFWCommands')
# client.load_extension('cogs.NSFW')
# client.load_extension('cogs.Games_and_Fun')
# client.load_extension('cogs.IslamQa')
# client.load_extension('cogs.Translator')
# client.load_extension('cogs.Hadith')

client.run(os.environ['BOT_TOKEN'])
