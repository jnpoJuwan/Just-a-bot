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

    @commands.command(aliases=['jsd', 'docs'])
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
                             icon_url=ctx.author.avatar.url)

            page_list.append(embed)
            i += 1

        paginator = ListPaginator(ctx, page_list)
        await paginator.start()

    @commands.command(aliases=['jsg', 'guidelines'])
    @commands.cooldown(2, 30.0, commands.BucketType.user)
    async def just_some_guidelines(self, ctx, pagination='on'):
        """Sends Just some guidelines....

        The is_paginated setting can be turned either on or off.
        """
        true_values = ['1', 'on', 'true', 'yes']
        false_values = ['0', 'off', 'false', 'no']

        pagination = pagination.lower()

        if pagination not in true_values and pagination not in false_values:
            raise commands.BadArgument

        # SEE: https://docs.google.com/document/d/1NAH6GZNC0UNFHdBmAd0u9U5keGhAgnxY-vqiRaATL8c/edit?usp=sharing
        guideline_lines = open('bot/assets/text/amino_guidelines.md', encoding='utf-8').readlines()

        # raw_page_list is made of dictionaries (pages) containing the heading and contents.
        raw_page_list = [{}]

        for index, value in enumerate(guideline_lines[1:]):
            if value.startswith('# ') or len(raw_page_list[-1]) >= 24:
                raw_page_list.append({})

            if value.startswith('## '):
                page_content = ''.join(guideline_lines[index + 2: index + 5])[:-1]
                raw_page_list[-1][value[3:-1]] = page_content

        page_list = []
        i = 1

        if pagination in false_values:
            for page in raw_page_list:
                embed = discord.Embed(title='Just some guidelines...', colour=COLOUR)
                for k, v in page.items():
                    embed.add_field(name=k, value=v)

                if page == raw_page_list[-1]:
                    embed.set_footer(text=f'Requested by {ctx.author.display_name}',
                                     icon_url=ctx.author.avatar.url)
                await ctx.send(embed=embed)
        else:
            for page in raw_page_list:
                embed = discord.Embed(title='Just some guidelines...', colour=COLOUR)
                for k, v in page.items():
                    embed.add_field(name=k, value=v)
                embed.set_footer(text=f'Requested by {ctx.author.display_name} | Page {i}/{len(raw_page_list)}',
                                 icon_url=ctx.author.avatar.url)

                page_list.append(embed)
                i += 1

            paginator = ListPaginator(ctx, page_list)
            await paginator.start()

    @just_some_guidelines.error
    async def just_some_guidelines_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('The paginated setting must be turned either on or off.')

    @commands.command(aliases=['jstz', 'timezones', 'time_zones'])
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

        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(JustAChat(bot))
