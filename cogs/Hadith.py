import requests
import discord
import asyncio
import bs4
from bs4 import BeautifulSoup
from discord.ext import commands
from urllib.parse import urlencode

from re import finditer, search


authors = {'bukhari':'Sahih Bukhari',
            'muslim':'Sahih Muslim',
            'tirmidhi':'Jami` at-Tirmidhi',
            'abudawud':'Sunan Abi Dawud',
            'nasai':"Sunan an-Nasa'i",
            'ibnmajah':'Sunan Ibn Majah',
            'malik':'Muwatta Malik',
            'riyadussaliheen':'Riyad as-Salihin',
            'adab':"Al-Adab Al-Mufrad",
            'bulugh':'Bulugh al-Maram',
            'qudsi40':'40 Hadith Qudsi',
            'nawawi40':'40 Hadith Nawawi'}

exception_hadiths = {'qudsi':'qudsi40','nawawi':'nawawi40'}

class Hadith(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hadith is Prepared')

    @commands.command(
        pass_context=True
        )
    async def hadith(self, ctx, bookAuthor:str, bookNumber:str, hadithNumber:str=None):

        async with ctx.typing():
            await asyncio.sleep(.05)

        #parsing
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

        if hadithNumber == None: #catching cuntish author structures
            url = "https://sunnah.com/"+ bookAuthor.lower() + "/" + bookNumber # Capitalisation from user won't matter anymore with .lower()
        else:
            url = "https://sunnah.com/"+ bookAuthor.lower() + "/" + bookNumber + "/" + hadithNumber # Capitalisation from user won't matter anymore with .lower()

        webPage = requests.get(url, headers= headers) # Capitalisation from user won't matter anymore with .lower()
        dataSet = bs4.BeautifulSoup(webPage.text, 'lxml')

        # catching errors  NEEDS WORK
        error_load = dataSet.find_all(class_ = "mainContainer")
        error_stripped = [cunt_bugs.text.strip() for cunt_bugs in error_load]
        error_message = "You have entered an incorrect URL. Please use the menu above to navigate the website"

        if 'incorrect' in error_stripped[0] is True :
            await ctx.say('Thats an invalid Hadith reference or you typed something wrong. Double check and try again !')

        else:
            # specific classes we are after
            bookname_english = dataSet.find_all(class_ = "book_page_english_name") #only saying book, not full name fix later

            bookname_arabic = dataSet.find_all(class_ = "book_page_arabic_name arabic")

            hadith_parsed_english = dataSet.find_all(class_ = "english_hadith_full")

            hadith_parsed_arabic = dataSet.find_all(class_ = "arabic_hadith_full arabic")



            # stripped data
            stripped_bookname_english = [bookE.text.strip() for bookE in bookname_english]

            stripped_bookname_arabic = [bookA.text.strip() for bookA in bookname_arabic]

            stripped_hadith_english = [hadithE.text.strip() for hadithE in hadith_parsed_english]

            stripped_hadith_arabic = [hadithA.text.strip() for hadithA in hadith_parsed_arabic]

            for tr in dataSet.find_all(class_ = "hadith_reference"): #parsing tables are a cunt
                stripped_reference = [item.text.strip() for item in tr.find_all("tr")]

            try:
                embed = discord.Embed(
                        title = (stripped_bookname_english[0]),
                        description = (stripped_hadith_english[0]),
                        url= url,
                        colour=0xb30446,
                        )
                embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Hadith1.png/200px-Hadith1.png')
                embed.add_field(name= (stripped_bookname_arabic[0]) ,value= (stripped_hadith_arabic[0]) , inline=False)
                embed.add_field(name= "References :" ,value=
                    (stripped_reference[0]) + "\n" +
                    (stripped_reference[1]) + "\n" +
                    (stripped_reference[2]) + "\n" +
                    (stripped_reference[3])
                    , inline=True)

                await ctx.send(embed=embed)

            except Exception: #catch long hadiths
                if stripped_hadith_english[0:+500]:

                    embed = discord.Embed(
                            title = "The Hadith is too long for me to post here",
                            description = "Heres a link to the full text:",
                            url= url,
                            colour=0xb70000,
                            )

                    await ctx.send(embed=embed)
                    await ctx.send(url)

def setup(client):
    client.add_cog(Hadith(client))
