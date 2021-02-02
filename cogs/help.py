import asyncio
import json

import discord
from discord.ext import commands

from ._utils.constants import COLOUR

FIRST_EMOJI = '\u23ee'
LEFT_EMOJI = '\u2b05'
DELETE_EMOJI = '\U0001f5d1\ufe0f'
RIGHT_EMOJI = '\u27a1'
LAST_EMOJI = '\u23ed'

PAGINATION_EMOJI = (FIRST_EMOJI, LEFT_EMOJI, DELETE_EMOJI, RIGHT_EMOJI, LAST_EMOJI)


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.help_command = None

    @commands.command(aliases=['info'])
    async def help(self, ctx):
        """Send an embed with the Just a bot...'s information and a section of its commands."""
        file = open('configs/prefixes.json')
        p = json.load(file)[str(ctx.message.guild.id)]

        current_page = 0
        # HACK: Using a list with tuples of the page contents.
        pages = [
            # Page 0
            (
                ('Miscellaneous Commands',
                 f'►`{p}help` sends this message!\n'
                 f'►`{p}8ball [question]` asks the *Magic 8-Ball* for answers.\n'
                 f'►`{p}cbt` sends the Wikipedia summary and page for Cock and Ball Torture.\n'
                 f'►`{p}echo [message]` (or `{p}say [message]`) echoes the message.\n'
                 f'►`{p}penis [@member]` sends a member\'s dick length.\n'
                 f'►`{p}umlaut [message]` sënds yöür sëntëncë wïth ümläüts.\n'
                 f'►`{p}hello` Hi!\n'
                 f'►`{p}ping` Pong.'),
                ('Action Commands',
                 f'►`{p}cry` makes you cry.\n'
                 f'►`{p}cum` (or `{p}cream <@member>`) cums (inside the member).\n'
                 f'►`{p}cuddle <@member>` cuddles the member.\n'
                 f'►`{p}hold_hands <@member>` holds hands with the member.\n'
                 f'►`{p}hug <@member>` hugs the member.\n'
                 f'►`{p}fuck <@member>` fucks the member\'s arse.)\n'
                 f'►`{p}kill <@member>` murders the member.\n'
                 f'►`{p}kiss <@member>` kisses the member.\n'
                 f'►`{p}moan` makes you moan.\n'
                 f'►`{p}poke <@member>` pokes the member.\n'
                 f'►`{p}scream` makes you scream.\n'
                 f'►`{p}slap <@member>` slaps the member in the face.\n'
                 f'►`{p}suck` (or `{p}suq`) sucks the member.')
            ),

            # Page 1
            (
                ('Administration/Moderation Commands',
                 f'►`{p}ban <@member> (reason)` bans the member.\n'
                 f'►`{p}configs prefix [prefix]` changes the server\'s prefix.\n'
                 f'►`{p}kick <@member> (reason)` kicks the member.\n'
                 f'►`{p}mute` mutes the member.\n'
                 f'►`{p}purge [amount]` (or `{p}clear [amount]`) deletes the amount of messages.\n'
                 f'►`{p}unban <user_id>` unbans the user.\n'
                 f'►`{p}unmute` unmutes the member.'),
            ),

            # Page 2
            (
                ('Utility Commands',
                 f'►`{p}choose [list]` randomly chooses an item of choice.\n'
                 f'►`{p}coin_flip [amount]` flips a coin an amount of times.\n'
                 f'►`{p}eval [code]` evaluates Python code.\n'
                 f'►`{p}get_prefix` sends the server\'s prefix.\n'
                 f'►`{p}poll [question]` creates a poll for a question.\n'
                 f'►`{p}random` sends a fractional random number between 0 and 1.\n'
                 f'►`{p}roll [die] [amount]` rolls a die of a input number an amount of times.\n'),
                ('Meta Commands',
                 f'►`{p}member [@member]` sends the member\'s information.\n'
                 f'►`{p}pfp [@member]` sends the member\'s profile picture.\n'
                 f'►`{p}server` sends the server\'s information.\n'
                 f'►`{p}source_code` sends the link to the bot\'s GitHub repository.'),
                ('Just a chat... Commands',
                 f'►`{p}jsdocs` (or `{p}jsd`) sends Just some documents....\n'
                 f'►`{p}jsguidelines` (or `{p}jsg`) sends Amino Just some guidelines.\n'
                 f'►`{p}jstimezones` (or `{p}jstz`) sends JACers\' date and times.\n'
                 f'►`{p}jsyoutube` or (`{p}jsyt`) sends Just a chat... YouTubers\' channels and videos.')
            )
        ]

        embed = discord.Embed(title='Help', colour=COLOUR)
        for section in pages[current_page]:
            embed.add_field(name=section[0], value=section[1], inline=False)
        footer = f'Requested by {ctx.author.name} | Page {current_page + 1}/{len(pages)}'
        embed.set_footer(text=footer, icon_url=ctx.author.avatar_url)

        message = await ctx.send(embed=embed)

        # CREDIT: @python-discord (GitHub [https://github.com/python-discord/bot/blob/master/bot/pagination.py])
        def event_check(reaction_: discord.Reaction, user_: discord.Member):
            return (
                # Conditions for a successful pagination:
                all((
                    # Reaction is on the help message.
                    reaction_.message.id == message.id,
                    # Reaction is a pagination emoji.
                    str(reaction_.emoji) in PAGINATION_EMOJI,
                    # Reaction was not made by the bot.
                    user_.id != ctx.bot.user.id
                ))
            )

        for emoji in PAGINATION_EMOJI:
            await message.add_reaction(emoji)

        while True:
            try:
                reaction, user = await ctx.bot.wait_for('reaction_add', timeout=300.0, check=event_check)
            except asyncio.TimeoutError:
                await message.clear_reactions()
                embed.set_footer(text=f'Requested by {ctx.author.name} | Paginator timed out',
                                 icon_url=ctx.author.avatar_url)
                await message.edit(embed=embed)
                break

            if str(reaction.emoji) == DELETE_EMOJI:
                return await message.delete()

            if reaction.emoji == FIRST_EMOJI:
                await message.remove_reaction(reaction.emoji, user)
                current_page = 0

                embed.clear_fields()
                for section in pages[current_page]:
                    embed.add_field(name=section[0], value=section[1], inline=False)
                embed.set_footer(text=f'Requested by {ctx.author.name} | Page {current_page + 1}/{len(pages)}',
                                 icon_url=ctx.author.avatar_url)
                await message.edit(embed=embed)

            if reaction.emoji == LAST_EMOJI:
                await message.remove_reaction(reaction.emoji, user)
                current_page = len(pages) - 1

                embed.clear_fields()
                for section in pages[current_page]:
                    embed.add_field(name=section[0], value=section[1], inline=False)
                embed.set_footer(text=f'Requested by {ctx.author.name} | Page {current_page + 1}/{len(pages)}',
                                 icon_url=ctx.author.avatar_url)
                await message.edit(embed=embed)

            if reaction.emoji == LEFT_EMOJI:
                await message.remove_reaction(reaction.emoji, user)

                if current_page <= 0:
                    continue
                current_page -= 1

                embed.clear_fields()
                for section in pages[current_page]:
                    embed.add_field(name=section[0], value=section[1], inline=False)
                embed.set_footer(text=f'Requested by {ctx.author.name} | Page {current_page + 1}/{len(pages)}',
                                 icon_url=ctx.author.avatar_url)
                await message.edit(embed=embed)

            if reaction.emoji == RIGHT_EMOJI:
                await message.remove_reaction(reaction.emoji, user)

                if current_page >= len(pages) - 1:
                    continue
                current_page += 1

                embed.clear_fields()
                for section in pages[current_page]:
                    embed.add_field(name=section[0], value=section[1], inline=False)
                embed.set_footer(text=f'Requested by {ctx.author.name} | Page {current_page + 1}/{len(pages)}',
                                 icon_url=ctx.author.avatar_url)
                await message.edit(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
