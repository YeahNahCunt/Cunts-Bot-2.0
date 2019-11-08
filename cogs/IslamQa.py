import discord
import requests
import bs4
import asyncio
from discord.ext import commands
from bs4 import BeautifulSoup
from urllib.parse import urlencode


class IslamQa(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('IslamQa is Prepared')


    @commands.command(
        pass_context=True
        )
    async def islamqa(self, ctx):  #temp till I can add search functionality to the below script
        async with ctx.typing():

            avatar = ctx.message.author.avatar_url

            author = ctx.message.author

            url = 'https://islamqa.info/en/' ##for home

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

            resp = requests.get(url, headers= headers)

            soup = bs4.BeautifulSoup(resp.text, 'lxml')

            #Finding title of each post#
            find_title = soup.find_all("p", {"class": "has-font-content card-title"})
            stripped_title = [title.text.strip() for title in find_title] #print (stripped_title[0:5])

            #Finding link of each post#
            find_link = soup.find_all("a", {"class": "card post-card hovered_color"})
            stripped_link = [link['href'].strip() for link in find_link] #print (stripped_link[0:5])

            embed = discord.Embed( title = 'IslamQA.info',
                    description = 'Below is the newest questions being asked on islamqa.info:',
                    url= 'https://islamqa.info/en/',
                    colour=0x00ff80,
                    )
            embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1037548705946259456/xLdCqDOF_400x400.jpg')
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name + '  |||  Search function coming soon' )

            embed.add_field(name= '1. '+(stripped_title[0]) ,value= 'Link to answer:\n'+(stripped_link[0]) , inline=False)
            embed.add_field(name= '2. '+(stripped_title[1]) ,value= 'Link to answer:\n'+(stripped_link[1]) , inline=False)
            embed.add_field(name= '3. '+(stripped_title[2]) ,value= 'Link to answer:\n'+(stripped_link[2]) , inline=False)
            embed.add_field(name= '4. '+(stripped_title[3]) ,value= 'Link to answer:\n'+(stripped_link[3]) , inline=False)
            embed.add_field(name= '5. '+(stripped_title[4]) ,value= 'Link to answer:\n'+(stripped_link[4]) , inline=False)

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(IslamQa(client))
