import json

import discord
from discord.ext import commands

from .embeds import COLOUR


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # NOTE: This doesn't substitute the `!help` command.
    #  FIXME: Add a prettier `help!` command.
    @commands.command(aliases=["commands", "information"])
    async def info(self, ctx, section=1):
        """Send an embed with the Just a bot...'s information and a section of its commands."""
        if section <= 0:
            raise commands.BadArgument
        else:
            with open("configs/prefixes.json") as pf:
                prefixes = json.load(pf)
                p = prefixes[str(ctx.message.guild.id)]

            async with ctx.typing():
                embed = discord.Embed(
                    title="Just a bot...",
                    description="**Just a bot...** (**JAB**) is a personal Discord bot built written with "
                                "[discord.py](https://github.com/Rapptz/discord.py). This bot was developed for "
                                "playing around with creating a bot for some "
                                "[Just a chat...](https://aminoapps.com/c/conlang-conscript/home/)-related servers.",
                    colour=COLOUR)

            if section == 1:
                async with ctx.typing():
                    embed_ext = discord.Embed(
                        title="Miscellaneous Commands (1/3)",
                        description=f"►`{p}info [section]` sends information regarding this bot.\n"
                                    f"►`{p}8ball [question]` asks the *Magic 8-Ball* for answers.\n"
                                    f"►`{p}choose [list]` randomly chooses an item of choice.\n"
                                    f"►`{p}choose_map` (or `{p}map`) randomly chooses an Among Us map.\n"
                                    f"►`{p}direct_message` (or `!dm`) direct messages you a nice message.\n"
                                    f"►`{p}echo [message]` (or `{p}say [message]`) echoes the message.\n"
                                    f"►`{p}penis [@member]` sends a member's dick length.\n"
                                    f"►`{p}spam [amount] [message]` spams a message an given amount of times.\n"
                                    f"►`{p}umlaut [message]` sënds yöür sëntëncë wïth ümläüts.\n"
                                    f"►`{p}ping` Pong.",
                        colour=COLOUR)
                    embed_ext.add_field(name="Action Commands",
                                        value=f"►`{p}kiss [member]` kisses the member.\n"
                                              f"►`{p}fuck [member]` fucks the member's arse.\n"
                                              f"►`{p}poke [member]` pokes the member.\n"
                                              f"►`{p}slap [member]` slaps the member in the face.")
            elif section == 2:
                async with ctx.typing():
                    embed_ext = discord.Embed(
                        title="Administration Commands (2/3)",
                        description=f"►`{p}ban <@member> (reason)` bans the member.\n"
                                    f"►`{p}kick <@member> (reason)` kicks the member.\n"
                                    f"►`{p}change_prefix [prefix]` changes the server's prefix.\n"
                                    f"►`{p}purge [amount]` (or `{p}clear (num)`) purges the amount of messages.\n"
                                    f"►`{p}unban <user_id>` unbans the user.",
                        colour=COLOUR)
            elif section == 3:
                async with ctx.typing():
                    embed_ext = discord.Embed(
                        title="Utility Commands (3/3)",
                        description=f"►`{p}coin_flip [amount]` flips a coin an amount of times.\n"
                                    f"►`{p}eval [command]` evaluates the Python code."
                                    f"►`{p}get_prefix` sends the server's prefix.\n"
                                    f"►`{p}length [message]` sends the message's length.\n"
                                    f"►`{p}poll [question]` creates a poll for a question.\n"
                                    f"►`{p}random` sends a fractional random number between 0 and 1.\n"
                                    f"►`{p}roll [die] [amount]` rolls a die of a input number, "
                                    f"which is 20 by default, an amount of times.\n"
                                    f"►`{p}source_code` sends the link to the bot's GitHub repository."
                                    f"►`{p}words [message]` sends the number of words in the message.",
                        colour=COLOUR)
                    embed_ext.add_field(
                        name="Information Commands",
                        value=f"►`{p}member [@member]` sends the member's information.\n"
                              f"►`{p}pfp [@member]` sends the member's profile picture.\n"
                              f"►`{p}server` sends the server's information.",
                        inline=False)
                    embed_ext.add_field(
                        name="Just a chat... Commands",
                        value=f"►`{p}jsdocs` (or `{p}jsd`) sends Just some documents....\n"
                              f"►`{p}jsguidelines` (or `{p}jsg`) sends Amino Just some guidelines.\n"
                              f"►`{p}jstimezones` (or `{p}jstz`) sends JACers' date and times.\n"
                              f"►`{p}jsyoutube` or (`{p}jsyt`) sends some Just a chat... YouTubers' "
                              f"channels and videos.\n",
                        inline=False)
            else:
                raise commands.BadArgument

            embed_ext.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed_ext)

    # Exception Handler.

    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please insert a positive integer less or equal to 3.")


def setup(bot):
    bot.add_cog(Help(bot))
