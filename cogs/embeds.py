import datetime

import discord
from discord.ext import commands
from pytz import timezone, utc

from just_a_bot.utils import checks

COLOUR = discord.Colour(0x8b0000)


class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command(aliases=["cock_and_ball_torture"])
    async def cbt(self, ctx):
        """Send an embed with the summary for the Wikipedia page of "Cock and ball torture"."""
        async with ctx.typing():
            summary = "**Cock and ball torture** (**CBT**), penis torture or dick torture is a sexual activity " \
                      "involving application of pain or constriction to the penis or testicles." \
                      "This may involve directly painful activities, such as genital piercing, wax play, genital " \
                      "spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic " \
                      "electrostimulation, kneeing or kicking. The recipient of such activities may receive direct " \
                      "physical pleasure via masochism, or emotional pleasure through erotic humiliation, " \
                      "or knowledge that the play is pleasing to a sadistic dominant. " \
                      "Many of these practices carry significant health risks."

            embed = discord.Embed(title="Cock and ball torture", description=summary, colour=COLOUR)
            embed.add_field(name="External Link", value="https://en.wikipedia.org/wiki/Cock_and_ball_torture")
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def credits(self, ctx):
        """Send an embed with the credits for the bot."""
        async with ctx.typing():
            embed = discord.Embed(title="Credits", description="Made by <@488828457703309313>", colour=COLOUR)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    # NOTE: "js" here is the abbreviation "Just some", not "JavaScript".

    @commands.command(aliases=["jd", "jt", "jsd", "jst", "just_some_documents", "just_some_texts"])
    @checks.is_jsguilds()
    async def jsdocs(self, ctx):
        """Send an embed with the Just some documents...."""
        async with ctx.typing():
            embed_values = {
                "Just a map...": "https://goo.gl/maps/Z3VDj5JkwpVrDUSd7",
                "Just a (fuck-able) ages...":
                    "https://docs.google.com/document/d/1xeAlaHXVZ4PfFm_BrOuAxXrO-0SBZZZvZndCpI0rkDc/edit?usp=sharing",
                "Just some penises...":
                    "https://docs.google.com/document/d/1gUoTqg4uzdSG_0eqoERcbMBFBrWdIEw6IBy_L3OrRnQ/edit?usp=sharing",
                "Just some stories...":
                    "https://docs.google.com/document/d/1EGwg2vBL6VHaXK0B0u1mEXGV8SE9w6Xr1axlN8rB-Ic/edit?usp=sharing",
                "Just some units of measurement...":
                    "https://docs.google.com/document/d/1Zk1unIM76WaBvOh1ew04nEbSPxH1Gq54M3Tu4Znj05A/edit?usp=sharing",
                "(Extended) International Phonetic Alphabet":
                    "https://docs.google.com/spreadsheets/d/1Rx8ui5eug2Qk__B9IQkxVxFkdZaxbDkgGI2xNicqbtM"
                    "/edit?usp=sharing",
            }

            embed = discord.Embed(title="Just some documents...", colour=COLOUR)
            for k, v in embed_values.items():
                embed.add_field(name=k, value=v)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["jtz", "jstz", "just_some_timezones", "just_some_time_zones"])
    @checks.is_jsguilds()
    async def jstimezones(self, ctx):
        """Send an embed with Just a chat... users' time zones."""
        async with ctx.typing():
            dt = datetime.datetime.now(tz=utc)
            fmt = "%A, %B %d **%H:%M** UTC%z"
            # FIXME: Too time inefficient.
            tz_values = {
                ":flag_mx: Mexico (Pacific)": timezone("Mexico/BajaSur"),
                ":flag_um: USA (Mountain)": timezone("US/Mountain"),
                ":flag_mx: Mexico (Central)": timezone("Mexico/General"),
                ":flag_us: US (Central)": timezone("US/Central"),
                ":flag_um: USA (Eastern)": timezone("US/Eastern"),
                ":flag_py: Paraguay": timezone("America/Asuncion"),
                ":flag_br: Brazil (Brasília)": timezone("Brazil/East"),
                ":flag_eu: Europe (Western)": timezone("Europe/London"),
                ":flag_eu: Europe (Central)": timezone("Europe/Berlin"),
                ":flag_eu: Europe (Eastern)": timezone("Europe/Athens"),
                ":flag_ae: United Arab Emirates": timezone("Asia/Dubai"),
                ":flag_kr: South Korea": timezone("Asia/Seoul"),
            }

            embed = discord.Embed(title="Just some time zones...", colour=COLOUR)
            for key, value in tz_values.items():
                embed.add_field(name=key, value=str(dt.astimezone(value).strftime(fmt)))
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["jyt", "jsyt", "youtube"])
    @checks.is_jsguilds()
    async def jsyoutube(self, ctx):
        """Send Just a chat... user's YouTube channels."""
        channel_values = {
            "Aurora": "https://www.youtube.com/channel/UCmDE7oQp2wzTLxd7lc4mA9A",
            # "Daniel Lousada": "https://www.youtube.com/channel/UCCIjCbmgxW8XX-bz8viJsSg",
            "D'ignoranza": "https://www.youtube.com/channel/UCI4ZJ0QmSokr6ctUfURqm5A",
            "Dr. IPA": "https://www.youtube.com/channel/UCfPYxsZHRBaW24q3pb9oOnA",
            "Dracheneks": "https://www.youtube.com/channel/UCiaOA8yjnuZX5wUqmlRDUuA",
            # "Eddie R": "https://www.youtube.com/channel/UClHva_pJ44MSFgQV2HcKwPA",
            # "jnpoJuwan": "https://www.youtube.com/channel/UC5EgKQdEcCCpXK-Dz_heXFg",
            "MAGNVS": "https://www.youtube.com/channel/UC2AcuqQOPxH6pkbJs-xm_Qw",
            # "meni M": "https://www.youtube.com/channel/UCnYAJXIH9emHnhAZKBDTzSw",
            "PD6": "https://www.youtube.com/channel/UCuAsPOh-qA7wakswF6ioo4g",
            # "Zhivämky": "https://www.youtube.com/channel/UCz4nPEpO9cqd_sV7JgHVE0w"
        }
        video_values = {
            '"David Peterson Stole My Glottis! (Not Clickbait) #huntedmyglottis", by Dr. IPA':
                "https://youtu.be/RB0TTxSayaU",
            '"Epithet Erased but it\'s a Plotagon and I\'m poor | EP1 - Quiet in the Museum!", by PD6':
                "https://youtu.be/1nYESDnpoq8",
            '"Epithet Erased but it\'s a Plotagon and I\'m poor | EP2 - Bear Trap", by PD6':
                "https://youtu.be/3HvEcXplMGM",
        }

        async with ctx.typing():
            channels = discord.Embed(name="Just some channels...", colour=COLOUR)
            videos = discord.Embed(name="Just some videos...", colour=COLOUR)
            for k, v in channel_values.items():
                channels.add_field(name=k, value=v)
            for k, v in video_values.items():
                videos.add_field(name=k, value=v, inline=False)

            videos.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=channels)
        await ctx.send(embed=videos)

    @commands.command()
    async def poll(self, ctx, *, question):
        embed = discord.Embed(title="Poll", description=question, colour=COLOUR)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        # await ctx.send(embed=embed)
        message = await ctx.send(embed=embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷')

    @commands.command(aliases=["this"])
    async def zen(self, ctx):
        """Send "The Zen of Python", by Tim Peters."""
        zen = """Beautiful is better than ugly.
                 Explicit is better than implicit.
                 Simple is better than complex.
                 Complex is better than complicated.
                 Flat is better than nested.
                 Sparse is better than dense.
                 Readability counts.
                 Special cases aren't special enough to break the rules.
                 Although practicality beats purity.
                 Errors should never pass silently.
                 Unless explicitly silenced.
                 In the face of ambiguity, refuse the temptation to guess.
                 There should be one-- and preferably only one --obvious way to do it.
                 Although that way may not be obvious at first unless you're Dutch.
                 Now is better than never.
                 Although never is often better than *right* now.
                 If the implementation is hard to explain, it's a bad idea.
                 If the implementation is easy to explain, it may be a good idea.
                 Namespaces are one honking great idea -- let's do more of those!"""

        embed = discord.Embed(title="The Zen of Python, by Tim Peters", description=zen, colour=COLOUR)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Embeds(bot))
