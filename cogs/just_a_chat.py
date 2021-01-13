import datetime

import discord
from discord.ext import commands
from pytz import timezone, utc

from ._utils.constants import COLOUR
from ._utils import checks


class JustAChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'INFO: {__name__} is ready.')

    # GLOSS: 'js' means 'Just some', not 'JavaScript'.

    @commands.command(aliases=['jsd', 'just_some_documents'])
    @checks.is_jsguilds()
    async def jsdocs(self, ctx):
        """Send an embed with the Just some documents...."""
        embed_values = {
            'Just a bot...': 'https://github.com/jnpoJuwan/Just-a-bot',
            'Just a map...': 'https://goo.gl/maps/Z3VDj5JkwpVrDUSd7',
            'Just some (fuck-able) ages...':
                'https://docs.google.com/document/d/1xeAlaHXVZ4PfFm_BrOuAxXrO-0SBZZZvZndCpI0rkDc/edit?usp=sharing',
            'Just some guidelines...':
                'https://docs.google.com/document/d/1NAH6GZNC0UNFHdBmAd0u9U5keGhAgnxY-vqiRaATL8c/edit?usp=sharing',
            'Just some penises...':
                'https://docs.google.com/document/d/1gUoTqg4uzdSG_0eqoERcbMBFBrWdIEw6IBy_L3OrRnQ/edit?usp=sharing',
            'Just some stories...':
                'https://docs.google.com/document/d/1EGwg2vBL6VHaXK0B0u1mEXGV8SE9w6Xr1axlN8rB-Ic/edit?usp=sharing',
            'Just some units of measurement...':
                'https://docs.google.com/document/d/1Zk1unIM76WaBvOh1ew04nEbSPxH1Gq54M3Tu4Znj05A/edit?usp=sharing',
            '(Extended) International Phonetic Alphabet':
                'https://docs.google.com/spreadsheets/d/1Rx8ui5eug2Qk__B9IQkxVxFkdZaxbDkgGI2xNicqbtM'
                '/edit?usp=sharing',
        }

        embed = discord.Embed(title='Just some documents...', colour=COLOUR)
        for k, v in embed_values.items():
            embed.add_field(name=k, value=v, inline=False)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['jstz'])
    @checks.is_jsguilds()
    async def jstimezones(self, ctx):
        """Send an embed with Just a chat... users' time zones."""
        await ctx.send('Calculating time zones...')

        # NOTE: ctx.typing() is used, since this command takes an *extremely* long time.
        async with ctx.typing():
            dt = datetime.datetime.now(tz=utc)
            fmt = '%A, %B %d **%H:%M** UTC%z'
            tz_values = {
                ':flag_mx: Mexico (Pacific)': timezone('Mexico/BajaSur'),
                ':flag_um: US (Mountain)': timezone('US/Mountain'),
                ':flag_mx: Mexico (Central)': timezone('Mexico/General'),
                ':flag_us: US (Central)': timezone('US/Central'),
                ':flag_um: US (Eastern)': timezone('US/Eastern'),
                ':flag_py: Paraguay': timezone('America/Asuncion'),
                ':flag_br: Brazil (Brasília)': timezone('Brazil/East'),
                ':flag_eu: Europe (Western)': timezone('Europe/London'),
                ':flag_eu: Europe (Central)': timezone('Europe/Berlin'),
                ':flag_eu: Europe (Eastern)': timezone('Europe/Athens'),
                ':flag_ae: United Arab Emirates': timezone('Asia/Dubai'),
                ':flag_kr: South Korea': timezone('Asia/Seoul'),
            }

            embed = discord.Embed(title='Just some time zones...', colour=COLOUR)
            for k, v in tz_values.items():
                embed.add_field(name=k, value=str(dt.astimezone(v).strftime(fmt)))
            embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['jsyt'])
    @checks.is_jsguilds()
    async def jsyoutube(self, ctx):
        """Send an embed with some Just a chat... user's YouTube channels."""
        channel_values = {
            'Aurora': 'https://www.youtube.com/channel/UCmDE7oQp2wzTLxd7lc4mA9A',
            # 'Daniel Lousada': 'https://www.youtube.com/channel/UCCIjCbmgxW8XX-bz8viJsSg',
            'D\'ignoranza': 'https://www.youtube.com/channel/UCI4ZJ0QmSokr6ctUfURqm5A',
            'Dr. IPA': 'https://www.youtube.com/channel/UCfPYxsZHRBaW24q3pb9oOnA',
            'Dracheneks': 'https://www.youtube.com/channel/UCiaOA8yjnuZX5wUqmlRDUuA',
            # 'Eddie R': 'https://www.youtube.com/channel/UClHva_pJ44MSFgQV2HcKwPA',
            # 'jnpoJuwan': 'https://www.youtube.com/channel/UC5EgKQdEcCCpXK-Dz_heXFg',
            'MAGNVS': 'https://www.youtube.com/channel/UC2AcuqQOPxH6pkbJs-xm_Qw',
            # 'meni M': 'https://www.youtube.com/channel/UCnYAJXIH9emHnhAZKBDTzSw',
            'PD6': 'https://www.youtube.com/channel/UCuAsPOh-qA7wakswF6ioo4g',
            # 'Zhivämky': 'https://www.youtube.com/channel/UCz4nPEpO9cqd_sV7JgHVE0w'
        }

        embed = discord.Embed(name='Just some channels...', colour=COLOUR)
        for k, v in channel_values.items():
            embed.add_field(name=k, value=v)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(JustAChat(bot))
