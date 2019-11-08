import discord
import json
from discord.ext import commands
from googletrans import Translator

client = discord.Client()

class Translate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Translator is Prepared')

##on reaction code for translations
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel_react = reaction.message.channel

        avatar = reaction.message.author.avatar_url
        author = reaction.message.author
        # user_avatar = reaction.me
        # user_name = reaction.users().flatten()

        ##api params
        translator = Translator()
        reply = translator.translate(reaction.message.content, dest='en').text
        lang_detect= translator.detect(reaction.message.content)
        detected_lang = lang_detect.lang

        # languages = int({
        #             "af": "afrikaans",
        #             "sq": "albanian",
        #             "am": "amharic",
        #             "ar": "arabic",
        #             "hy": "armenian",
        #             "az": "azerbaijani",
        #             "eu": "basque",
        #             "be": "belarusian",
        #             "bn": "bengali",
        #             "bs": "bosnian",
        #             "bg": "bulgarian",
        #             "ca": "catalan",
        #             "ceb": "cebuano",
        #             "ny": "chichewa",
        #             "zh-cn": "chinese (simplified)",
        #             "zh-tw": "chinese (traditional)",
        #             "co": "corsican",
        #             "hr": "croatian",
        #             "cs": "czech",
        #             "da": "danish",
        #             "nl": "dutch",
        #             "en": "english",
        #             "eo": "esperanto",
        #             "et": "estonian",
        #             "tl": "filipino",
        #             "fi": "finnish",
        #             "fr": "french",
        #             "fy": "frisian",
        #             "gl": "galician",
        #             "ka": "georgian",
        #             "de": "german",
        #             "el": "greek",
        #             "gu": "gujarati",
        #             "ht": "haitian creole",
        #             "ha": "hausa",
        #             "haw": "hawaiian",
        #             "iw": "hebrew",
        #             "hi": "hindi",
        #             "hmn": "hmong",
        #             "hu": "hungarian",
        #             "is": "icelandic",
        #             "ig": "igbo",
        #             "id": "indonesian",
        #             "ga": "irish",
        #             "it": "italian",
        #             "ja": "japanese",
        #             "jw": "javanese",
        #             "kn": "kannada",
        #             "kk": "kazakh",
        #             "km": "khmer",
        #             "ko": "korean",
        #             "ku": "kurdish (kurmanji)",
        #             "ky": "kyrgyz",
        #             "lo": "lao",
        #             "la": "latin",
        #             "lv": "latvian",
        #             "lt": "lithuanian",
        #             "lb": "luxembourgish",
        #             "mk": "macedonian",
        #             "mg": "malagasy",
        #             "ms": "malay",
        #             "ml": "malayalam",
        #             "mt": "maltese",
        #             "mi": "maori",
        #             "mr": "marathi",
        #             "mn": "mongolian",
        #             "my": "myanmar (burmese)",
        #             "ne": "nepali",
        #             "no": "norwegian",
        #             "ps": "pashto",
        #             "fa": "persian",
        #             "pl": "polish",
        #             "pt": "portuguese",
        #             "pa": "punjabi",
        #             "ro": "romanian",
        #             "ru": "russian",
        #             "sm": "samoan",
        #             "gd": "scots gaelic",
        #             "sr": "serbian",
        #             "st": "sesotho",
        #             "sn": "shona",
        #             "sd": "sindhi",
        #             "si": "sinhala",
        #             "sk": "slovak",
        #             "sl": "slovenian",
        #             "so": "somali",
        #             "es": "spanish",
        #             "su": "sundanese",
        #             "sw": "swahili",
        #             "sv": "swedish",
        #             "tg": "tajik",
        #             "ta": "tamil",
        #             "te": "telugu",
        #             "th": "thai",
        #             "tr": "turkish",
        #             "uk": "ukrainian",
        #             "ur": "urdu",
        #             "uz": "uzbek",
        #             "vi": "vietnamese",
        #             "cy": "welsh",
        #             "xh": "xhosa",
        #             "yi": "yiddish",
        #             "yo": "yoruba",
        #             "zu": "zulu",
        #             "fil": "Filipino",
        #             "he": "Hebrew"
        #             }.get(detected_lang,detected_lang))


        if reaction.emoji == '🇬🇧':  # United Kingdom flag (english translation)
            if reaction.count > 1:
                return
            else:

                # with open('languages.json') as f:
                #     data = json.load(f)

                # for language in data:
                #     lang_detect in data == category

                embed = discord.Embed(
                    title = author.name + " said:",
                    description = reaction.message.content,
                    color=0xff00ff,
                    )
                embed.set_thumbnail(url= 'https://i.imgur.com/rLY3z3E.png')
                embed.set_footer(text='Requested by: ' + user.name + "  |  Requested language: English" )
                embed.add_field(name="From that I've translated the following:", value=reply , inline=False)

                # embed.add_field(name="\u200b", value= "Just CUNT testing stuff here:\n" + languages.detected_lang()  , inline=True)

                await channel_react.send(embed=embed)
                # await channel_react.send(str(lang_detect.lang) + str(lang_detect.confidence))

        if reaction.emoji == '🇸🇦':  # Saudi flag (Arab translation)
            if reaction.count > 1:
                return
            else:
                translator = Translator()
                reply = translator.translate(reaction.message.content, dest='ar').text
                lang_detect= translator.detect(reaction.message.content)
                embed = discord.Embed(
                    title = author.name + " said:",
                    description = reaction.message.content,
                    color=0xff00ff,
                    )
                embed.set_thumbnail(url= 'https://i.imgur.com/rLY3z3E.png')
                embed.set_footer(text='Requested by: ' + user.name + "  |  Requested language: Arabic")
                embed.add_field(name="From that I've translated the following:", value=reply , inline=False)

                await channel_react.send(embed=embed)
                # await channel_react.send(lang_detect.lang + lang_detect.confidence)

        if reaction.emoji == '🇵🇹':  # Portugal flag (Portugese translation)
            if reaction.count > 1:
                return
            else:
                translator = Translator()
                reply = translator.translate(reaction.message.content, dest='pt').text
                lang_detect= translator.detect(reaction.message.content)
                embed = discord.Embed(
                    title = author.name + " said:",
                    description = reaction.message.content,
                    color=0xff00ff,
                    )
                embed.set_thumbnail(url= 'https://i.imgur.com/rLY3z3E.png')
                embed.set_footer(text='Requested by: ' + user.name + "  |  Requested language: Portugese")
                embed.add_field(name="From that I've translated the following:", value=reply , inline=False)

                await channel_react.send(embed=embed)
                # await channel_react.send(lang_detect.lang + lang_detect.confidence)

        if reaction.emoji == '🇫🇷':  # France flag (French translation)
            if reaction.count > 1:
                return
            else:
                translator = Translator()
                reply = translator.translate(reaction.message.content, dest='fr').text
                lang_detect= translator.detect(reaction.message.content)
                embed = discord.Embed(
                    title = author.name + " said:",
                    description = reaction.message.content,
                    color=0xff00ff,
                    )
                embed.set_thumbnail(url= 'https://i.imgur.com/rLY3z3E.png')
                embed.set_footer(text='Requested by: ' + user.name + "  |  Requested language: French")
                embed.add_field(name="From that I've translated the following:", value=reply , inline=False)

                await channel_react.send(embed=embed)
                # await channel_react.send(lang_detect.lang + lang_detect.confidence)


# #################### OWOify translator, easter egg function ########################################################################
#         if reaction.emoji == '🏳️‍🌈':
#             if reaction.count > 1:
#                 return
#             else:
#                 replace =   {"r": "l",
#                             "l": " w"
#                         }

#                 #custom replacement
#                 replace_s =  {"you"    : "yuwu",
#                             "god"    : "gowod",
#                             "and"    : "awnd",
#                             "the"    : "teh",
#                             "that"   : "thawt",
#                             "be"     : "bwe",
#                             "man"    : "mawn",
#                             "serpent": "sewpwent",
#                             "unto"   : "untwu",
#                             "to"     : "tuwu",
#                             "untrue" : "untwu",
#                             'knew'   : 'knuwu',
#                             'know'   : 'knowo',
#                             'so'     : 'sho',
#                             'no'     : 'nowo',
#                         }
#                 e = ''

#                 r = reaction.message.content.split()
#                 for word in r:
#                     if word.lower() in replace_s:
#                         if word.isupper():
#                             e += replace_s[word.lower()].capitalize()
#                         else:
#                             e += replace_s[word.lower()]
#                         e += " "
#                     else:
#                         for characters in word:
#                             if characters.lower() in replace:
#                                 if characters.isupper():
#                                     e += "W"
#                                 else:
#                                     e += "w"
#                             else:
#                                 e += characters
#                         e += " "
#                 if e.endswith(" "):
#                     e = e[:-1]
#                 await channel_react.send(e)

def setup(client):
    client.add_cog(Translate(client))
