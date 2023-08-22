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

    @commands.command(aliases=['jsd', 'docs'])
    async def just_some_docs(self, ctx):
        """Sends Just some documents...."""
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

    @commands.command(aliases=['jstz', 'timezones', 'time_zones'])
    async def just_some_timezones(self, ctx):
        """Sends Just a chat... users' time zones."""
        await ctx.send('Calculating times...')

        await ctx.trigger_typing()
        dt = datetime.datetime.now(tz=utc)
        # TODO: Move to JSON file at /assets
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
            ':flag_ae: UAE': timezone('Asia/Dubai'),
            ':flag_in: India': timezone('Asia/Kolkata'),
        }

        embed = discord.Embed(title='Just some time zones...', colour=COLOUR)
        for k, v in tz_dict.items():
            tz = str(dt.astimezone(v).strftime('%A, %d %B **%H:%M** UTC%z'))
            tz = tz[:-2] + ':' + tz[-2:]
            embed.add_field(name=k, value=tz)

        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(JustAChat(bot))
