import requests
import discord
import asyncio
import bs4
from bs4 import BeautifulSoup
from discord.ext import commands
from urllib.parse import urlencode

from re import finditer, search


# Translations = {Abdul Haleem = 85
# Dr. Ghali = 17
# Dr. Mustafa Khattab = 101
# Mufti Taqi Usmani = 84
# Muhsin Khan = 18
# Pickthall = 19
# Sahih International = 20
# Sayyid Abul Ala Maududi = 95
# Transliteration = 57
# Yusuf Ali = 22}


class Quran(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Quran is Prepared')

    @commands.command(
        pass_context=True
        )
    async def ayah(self, ctx,surah:str, verse:str, translator_author:str=None):

        async with ctx.typing():
            await asyncio.sleep(.05)

        if translator_author == None: #catching default author
            Translator = 11
        else: #Translator dictionary makes it easy to parse through each translator easily so I dont have make a bunch of if statements
            Translator = int({
            'ahmadali':'1', #Ahmad Ali
            'qarai':'2', # Ali Qarai
            'akhan':'3', #Ahmad Khan
            'arberry':'4', #Arberry
            'corpus':"5", #Corpus
            'daryabadi':'6', #Daryabadi
            'hilali':'7', #Hilali & Khan
            'maududi':'8', #Maududi
            'sarwar':"9", #Muhammad Sarwar
            'shakir':'10', #Muhammad Shakir
            'pickthall':'11', #Pickthall
            'qaribullah':'12', #Qaribullah
            'sahih':'13', # Sahih International
            'itani':'14', #Talal Itani
            'trans':"15", #Transliteration
            'wkhan':'16', # Wahihuddin Khan
            'yusufali':'17' #Yusuf Ali
            }.get(translator_author, translator_author))

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
        url = "https://quranx.com/" + surah + "." + verse
        webPage = requests.get(url, headers= headers)
        dataSet = bs4.BeautifulSoup(webPage.text, 'lxml')
        # specific classes we are after
        reference = dataSet.find_all(class_ = "verse__reference")[0].text.strip()
        arabic = dataSet.find_all(class_ = "arabic highlightable")[0].text.strip()
        translation_parse = dataSet.find_all(class_ = 'verse__translation' )[Translator].text.strip()

        embed = discord.Embed(
                        colour=0x00ffff,
                        )
        embed.set_thumbnail(url='http://3.bp.blogspot.com/-WSvzKmBv-6c/Vb91nGwfCeI/AAAAAAAAAZU/4j46GwFRub0/s1600/200px-Quran2.png')
        embed.add_field(name= (reference) ,value= (arabic) , inline=False)
        embed.add_field(name= (reference) ,value= (translation_parse) , inline=False)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Quran(client))
