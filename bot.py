import discord
import os
import random
import json
import asyncio
from discord.ext import commands

#clients or defining variables#

client = commands.Bot(command_prefix = '*')
client.remove_command('help')


#For Bot Debug and status#
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('*help'))
    print('Bot is ready.')
    print(discord.__version__)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('*******************')


@client.command()
async def ping(ctx):
    await ctx.send(f'Surprise motherfucker in {client.latency * 1000}ms')

@client.command()
async def pingNSFW(ctx):
    if  ctx.channel.is_nsfw():
        await ctx.send("Go for it you filthy animal")
    else :
        await ctx.send("You can't use that command here idiot! GO to a NSFW room!")


#help home#
@client.command()
async def help(ctx):
    await ctx.channel.trigger_typing()

    embed = discord.Embed(
        description = 'Below you will find a list of help commands that you can use with me',
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Cunts Bot Helpcenter')
    embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
    embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
    embed.add_field(name=':speech_balloon:  Translations :speech_balloon:', value= '`help_translations`', inline=False)
    embed.add_field(name=':kaaba:  Quran Translations :kaaba:', value= '`help_quran`', inline=False)
    embed.add_field(name=':baby_bottle: Safe for work commands :baby_bottle:', value= '`help_sfw`', inline=False)
    embed.add_field(name=':underage: NSFW commands :underage:', value= '`help_nsfw`', inline=False)
    embed.add_field(name=':vibration_mode:  Custom SubReddit Image searcher :vibration_mode: ', value= '`help_reddit`', inline=False)

    await ctx.send(embed=embed)

#translate help
@client.command()
async def help_translations(ctx):
    await ctx.channel.trigger_typing()

    embed = discord.Embed(
        description = 'Translation help centre instructions',
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Cunts Bot Helpcenter for Translations')
    embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
    embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
    embed.add_field(name=':speech_balloon:  Translations :speech_balloon: ', value=
    '`The bot can do translations for the following languages:`\n'+
    '\u200b\n'+ #cheat for line break
    'React to message with :flag_gb: for an ENGLISH translation\n'+
    'React to message with :flag_sa: for an ARABIC translation\n'+
    'React to message with :flag_pt:  for a PORTUGESE translation\n'+
    'React to message with :flag_fr:  for a FRENCH translation\n'+
    '\u200b\n'+
    'If you would like any other languages added to the functionality please contact Cunt ( Disturbed#3853 )',
    inline=False)
    await ctx.send(embed=embed)

#quran translations help
@client.command()
async def help_quran(ctx):
    await ctx.channel.trigger_typing()

    embed = discord.Embed(
        description = 'Quran Translation help centre instructions',
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Cunts Bot Helpcenter for Quran Translations')
    embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
    embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
    embed.add_field(name=':kaaba:  Quran Translations :kaaba: ', value=
    '\u200b\n'+
    'The format for fetching ayahs is:\n'+
    '\u200b\n'+ #cheat for line break
    '`*ayah {surah number} {verse number} {translator name}`\n'+
    '\u200b\n'+
    'Example:\n'+
    '\u200b\n'+
    '`*ayah 1 1 sahih`\n'
    '\u200b',
    inline=False)
    embed.add_field(name='Available Translations and their relavent index:', value=
    '\u200b\n'+
    'ahmadali = Ahmad Ali \n'+
    'qarai = Ali Qarai\n'+
    'akhan = Ahmad Khan\n'+
    'arberry = Arberry\n'+
    'corpus = Corpus\n'+
    'daryabadi = Daryabadi\n'+
    'hilali = Hilali & Khan\n'+
    'maududi = Maududi \n'+
    'sarwar = Muhammad Sarwar\n'+
    'shakir = Muhammad Shakir\n'+
    'pickthall = Pickthall  **(Default if no Translator is given)**\n'+
    'qaribullah = Qaribullah\n'+
    'sahih = Sahih International\n'+
    'itani = Talal Itani\n'+
    'trans = Transliteration\n'+
    'wkhan = Wahihuddin Khan\n'+
    'yusufali = Yusuf Ali\n'+
    '\u200b\n',
    inline=False)
    await ctx.send(embed=embed)

#SFW help
@client.command()
async def help_sfw(ctx):
    await ctx.channel.trigger_typing()

    embed = discord.Embed(
        description = 'Safe for general rooms help centre instructions',
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Cunts Bot Helpcenter for SFW')
    embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
    embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
    embed.add_field(name=':baby_bottle: Safe for work commands :baby_bottle:', value=
    '\u200b\n'+ #cheat for line break
    '`iwant memes        :` For dank Memes\n'+
    '`iwant gifs         :` For dank Gifs\n'+
    '`iwant aww          :` For all of the cuteness\n'+
    '`oicunt             :` Ask me questions\n'+
    '`ship               :` Who are you compatable with?\n'+
    '`insult             :` Mention someone else to get a sick burn\n'
    '`hug                :` Mention someone and send them some love\n'
    '`howgay             :` Mention yourself or someone else to find out how gay they are\n'+
    '`dong               :` Mention yourself or someone else to find out their dong length\n'+
    '`rekt               :` Mention yourself or someone else to find out how rekt they are\n'+
    '`flip               :` I flip tables\n'+
    '`rip {say something in quotation marks ""}:` Pay your respects\n'+
    '`islamqa            :` For the newest questions being asked on islamqa.info\n'
    '\u200b\n'
     , inline=False)
    await ctx.send(embed=embed)

#NSFW help
@client.command()
async def help_nsfw(ctx):
    if  ctx.channel.is_nsfw(): #checks if room is NSFW or not
        await ctx.channel.trigger_typing()

        embed = discord.Embed(
            description = 'NSFW help centre instructions',
            colour = discord.Colour.purple()
        )

        embed.set_author(name='Cunts Bot Helpcenter for NSFW')
        embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
        embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
        # embed.add_field(name=':underage: General NSFW :underage:', value=
        # '\u200b\n'+ #cheat for line break
        # '`nsfw amateur       :` Amateur girls\n'+
        # '`nsfw anal          :` For your anal fixations\n'+
        # '`nsfw ass           :` For some sweet booty\n'+
        # '`nsfw boobs         :` Mmmmhhh boobs\n'+
        # '`nsfw gonewild      :` random image from gonewild subreddit\n'
        # '`nsfw milf          :` Hot mommas\n'+
        # '`nsfw gifs          :` Sexy gifs\n'+
        # '`nsfw petite        :` Petite cute girls\n'+
        # '`nsfw teen          :` Legal teens\n'+
        # '\u200b' #cheat for line break
        # , inline=False)
        # embed.add_field(name=':fire: KINK NSFW :fire:', value=
        # '\u200b\n'+ #cheat for line break
        # '`nsfw blowjob       :` Sexy BJs\n'+
        # '`nsfw BDSM          :` Hot, sweaty and rough\n'+
        # '`nsfw celeb         :` Celebs and their best nude/sexy content\n'+
        # '`nsfw cum           :` We got your protein fix here\n'+
        # '`nsfw fit           :` Female Body Perfection\n'
        # '`nsfw gay           :` A place for sexy guys\n'+
        # '`nsfw lesbian       :` Girl on girl action\n'+
        # '`nsfw orgasm        :` "O" Faces. Faces of Ecstasy\n'+
        # '`nsfw outfits       :` Hot pics of people in NSFW Outfits\n'+
        # '`nsfw pussy         :` It is not about cats\n'+
        # '`nsfw thicc         :` Sexy curves\n'+
        # '`nsfw thigh         :` Thick thighs and luscious curves\n'+
        # '`nsfw trans         :` Traps and trans\n'+
        # '`nsfw hentai        :` Rule 34 an dother weeb trash\n'+
        # '\u200b' #cheat for line break
        # , inline=False)
        # embed.add_field(name=':earth_africa: Ethnic NSFW :earth_asia:', value=
        # '\u200b\n'+ #cheat for line break
        # '`nsfw ethnic        :` For your random exotic cravings\n'+
        # '`nsfw arab          :` Middle eastern hotties\n'+
        # '`nsfw asian         :` For that Eastern taste\n'+
        # '`nsfw black         :` Tastes like chocolate\n'+
        # '`nsfw latino        :` Hot blooded latin girls\n'
        # '`nsfw indian        :` Spicy indian girls\n'+
        # '`nsfw white         :` Pale cuties\n'+
        # '\u200b' #cheat for line break
        # , inline=False)
        embed.add_field(name=':mag: PORN SEARCH :mag_right: ', value=
        '\u200b\n'+ #cheat for line break
        '`fap                :` Get the most searched porn pic/gif online ATM\n'+
        '\u200b\n'+
        '`fap {your search query here}          :`\n'+
        'Returns a random pic or gif from your search query\n'+
        '`hub {your search query here}          :`\n'+
        'Returns a random pornhub.com gif from your search query\n'+
        '`fuck {someones username}:` Tag someone to fuck them\n'+
        '`lick {someones username}:` Tag someone to lick them out\n'+
        '`suck {someones username}:` Tag someone to suck them\n'+
        '\u200b' #cheat for line break
        , inline=False)
        await ctx.send(embed=embed)

    else :
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")

#Reddit help
@client.command()
async def help_reddit(ctx):
    await ctx.channel.trigger_typing()

    embed = discord.Embed(
        description = 'Reddit image search help centre instructions',
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Cunts Bot Helpcenter for Reddit image search')
    embed.set_thumbnail(url='https://i.imgur.com/nOePjfE.jpg')
    embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
    embed.add_field(name=':vibration_mode:  How it works :vibration_mode: ', value=
    'The bot can search any subreddit by doing the following:\n'+
    '\u200b\n'+ #cheat for line break
    '`sub {subreddit name}  :` After *sub add the subreddit you would like a random image/album/gif from\n'+
    '\u200b\n'+
    'Example :\n'+
    '`sub pics  :` Will return a image/album/gif from the  r/pics subreddit\n',
    inline=False)
    await ctx.send(embed=embed)



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
        
        
client.run(Auth.discord_token)        
