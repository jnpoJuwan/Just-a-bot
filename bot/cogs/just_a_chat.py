import datetime
import json

import discord
from discord.ext import commands
from pytz import timezone, utc

from ..utils.constants import COLOUR
from ..utils.paginator import ListPaginator


class JustAChat(commands.Cog, name='Just a chat...'):
    def __init__(self, bot):
        self.bot = bot

    # GLOSS: 'js' means 'Just some', not 'JavaScript'.

    @commands.command(aliases=['jacdocs', 'jsd', 'jsdocs'])
    async def just_some_docs(self, ctx):
        """Sends Just some documents...."""
        # CRED: @Tortoise-Community
        # (https://github.com/Tortoise-Community/Tortoise-BOT/blob/master/bot/utils/paginator.py)
        page_list = []

        await ctx.trigger_typing()
        raw_page_list = json.load(open('bot/assets/text/just_some_docs.json'))
        i = 1

        def add_content_formatting(content):
            docs_links = [f'[{text}]({url})' for text, url in content.items()]
            return '\n'.join(docs_links)

        for k, v in raw_page_list.items():
            embed = discord.Embed(title=k, description=add_content_formatting(v), colour=COLOUR)
            embed.set_footer(text=f'Requested by {ctx.author.display_name} | Page {i}/{len(raw_page_list)}',
                             icon_url=ctx.author.avatar_url)

            page_list.append(embed)
            i += 1

        paginator = ListPaginator(ctx, page_list)
        await paginator.start()

    @commands.command(aliases=['jacguidelines', 'jsg', 'jsguidelines'])
    @commands.cooldown(1, 60.0, commands.BucketType.user)
    async def just_some_guidelines(self, ctx):
        """Sends Just some guidelines...."""
        # SEE: https://docs.google.com/document/d/1NAH6GZNC0UNFHdBmAd0u9U5keGhAgnxY-vqiRaATL8c/edit?usp=sharing
        guideline_lines = open('bot/assets/text/amino_guidelines.md', encoding='utf-8').readlines()

        # raw_page_list is made of dictionaries (pages) containing the heading and contents.
        raw_page_list = [{}]

        for index, value in enumerate(guideline_lines[1:]):
            if value.startswith('# ') or len(raw_page_list[-1]) >= 24:
                raw_page_list.append({})

            if value.startswith('## '):
                page_content = ''.join(guideline_lines[index + 3: index + 6])[:-1]
                raw_page_list[-1][value[3:-1]] = page_content

        page_list = []
        i = 1

        for page in raw_page_list:
            embed = discord.Embed(title='Just some guidelines...', colour=COLOUR)
            for k, v in page.items():
                embed.add_field(name=k, value=v)
            embed.set_footer(text=f'Requested by {ctx.author.display_name} | Page {i}/{len(raw_page_list)}',
                             icon_url=ctx.author.avatar_url)

            page_list.append(embed)
            i += 1

        paginator = ListPaginator(ctx, page_list)
        await paginator.start()

    @just_some_guidelines.error
    async def just_some_guidelines_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('The paginated setting must be turned either on or off.')

    @commands.command(aliases=['jactimezones', 'jactz', 'jstimezones', 'jstz'])
    async def just_some_timezones(self, ctx):
        """Sends Just a chat... users' time zones."""
        await ctx.send('Calculating times...')

        await ctx.trigger_typing()
        dt = datetime.datetime.now(tz=utc)
        tz_dict = {
            ':flag_mx: Mexico (Pacific)': timezone('Mexico/BajaSur'),
            ':flag_us: US (Mountain)': timezone('US/Mountain'),
            ':flag_mx: Mexico (Central)': timezone('Mexico/General'),
            ':flag_us: US (Eastern)': timezone('US/Eastern'),
            ':flag_py: Paraguay': timezone('America/Asuncion'),
            ':flag_br: Brazil (Brasília)': timezone('Brazil/East'),
            ':flag_eu: Europe (Western)': timezone('Europe/London'),
            ':flag_eu: Europe (Central)': timezone('Europe/Berlin'),
            ':flag_eu: Europe (Eastern)': timezone('Europe/Athens'),
        }

        embed = discord.Embed(title='Just some time zones...', colour=COLOUR)
        for k, v in tz_dict.items():
            tz = str(dt.astimezone(v).strftime('%A, %d %B **%H:%M** UTC%z'))
            embed.add_field(name=k, value=tz[:-2] + ':' + tz[-2:])

        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['jacyoutube', 'jacyt', 'jsyoutube', 'jsyt'])
    async def just_some_youtube(self, ctx):
        """Send some Just a chat... users' YouTube channels."""
        channels_dict = {
            'Aurora': 'https://www.youtube.com/channel/UCmDE7oQp2wzTLxd7lc4mA9A',
            'D\'ignoranza': 'https://www.youtube.com/channel/UCI4ZJ0QmSokr6ctUfURqm5A',
            'Dr. IPA': 'https://www.youtube.com/channel/UCfPYxsZHRBaW24q3pb9oOnA',
            'Dracheneks': 'https://www.youtube.com/channel/UCiaOA8yjnuZX5wUqmlRDUuA',
            'MAGNVS': 'https://www.youtube.com/channel/UC2AcuqQOPxH6pkbJs-xm_Qw',
            'PD6': 'https://www.youtube.com/channel/UCuAsPOh-qA7wakswF6ioo4g',
        }

        embed = discord.Embed(name='Just some YouTube channels...', colour=COLOUR)
        for k, v in channels_dict.items():
            embed.add_field(name=k, value=v)

        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(JustAChat(bot))
