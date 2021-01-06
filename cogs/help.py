import json

import discord
from discord.ext import commands

from ._utils.constants import COLOUR


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # NOTE: This doesn't substitute the `!help` command.
    #  FIXME: Add a prettier !help command.
    @commands.command(aliases=["commands", "information"])
    async def info(self, ctx, section=1):
        """Send an embed with the Just a bot...'s information and a section of its commands."""
        with open("configs/prefixes.json") as f:
            p = json.load(f)[str(ctx.message.guild.id)]

        embed_ext0 = discord.Embed(
            title="Miscellaneous Commands",
            description=f"►`{p}info [page]` sends information regarding this bot.\n"
                        f"►`{p}8ball [question]` asks the *Magic 8-Ball* for answers.\n"
                        f"►`{p}cbt` sends the Wikipedia summary and page for Cock and Ball Torture.\n"
                        f"►`{p}choose [list]` randomly chooses an item of choice.\n"
                        f"►`{p}choose_map` (or `{p}map`) randomly chooses an Among Us map.\n"
                        f"►`{p}direct_message` (or `!dm`) direct messages you a nice message.\n"
                        f"►`{p}echo [message]` (or `{p}say [message]`) echoes the message.\n"
                        f"►`{p}penis [@member]` sends a member's dick length.\n"
                        f"►`{p}umlaut [message]` sënds yöür sëntëncë wïth ümläüts.\n"
                        f"►`{p}hello` Hi!\n"
                        f"►`{p}ping` Pong.",
            colour=COLOUR)
        embed_ext0.add_field(
            name="Action Commands",
            value=f"►`{p}kiss [member]` kisses the member.\n"
                  f"►`{p}fuck [member]` fucks the member's arse.\n"
                  f"►`{p}poke [member]` pokes the member.\n"
                  f"►`{p}slap [member]` slaps the member in the face.")
        embed_ext0.set_footer(text=f"Requested by {ctx.author.name} | Page 1/3", icon_url=ctx.author.avatar_url)

        embed_ext1 = discord.Embed(
            title="Administration Commands",
            description=f"►`{p}ban <@member> (reason)` bans the member.\n"
                        f"►`{p}settings prefix [prefix]` changes the server's prefix.\n"
                        f"►`{p}kick <@member> (reason)` kicks the member.\n"
                        f"►`{p}logout` logouts the bot.\n"
                        f"►`{p}purge [amount]` (or `{p}clear (num)`) purges the amount of messages.\n"
                        f"►`{p}unban <user_id>` unbans the user.",
            colour=COLOUR)
        embed_ext1.set_footer(text=f"Requested by {ctx.author.name} | Page 2/3", icon_url=ctx.author.avatar_url)

        embed_ext2 = discord.Embed(
            title="Utility Commands (3/3)",
            description=f"►`{p}coin_flip [amount]` flips a coin an amount of times.\n"
                        f"►`{p}eval [command]` evaluates the Python code.\n"
                        f"►`{p}get_prefix` sends the server's prefix.\n"
                        f"►`{p}length [message]` sends the message's length.\n"
                        f"►`{p}poll [question]` creates a poll for a question.\n"
                        f"►`{p}random` sends a fractional random number between 0 and 1.\n"
                        f"►`{p}roll [die] [amount]` rolls a die of a input number an amount of times.\n"
                        f"►`{p}source_code` sends the link to the bot's GitHub repository.\n"
                        f"►`{p}words [message]` sends the number of words in the message.",
            colour=COLOUR)
        embed_ext2.add_field(
            name="Information Commands",
            value=f"►`{p}member [@member]` sends the member's information.\n"
                  f"►`{p}pfp [@member]` sends the member's profile picture.\n"
                  f"►`{p}server` sends the server's information.",
            inline=False)
        embed_ext2.add_field(
            name="Just a chat... Commands",
            value=f"►`{p}jsdocs` (or `{p}jsd`) sends Just some documents....\n"
                  f"►`{p}jsguidelines` (or `{p}jsg`) sends Amino Just some guidelines.\n"
                  f"►`{p}jstimezones` (or `{p}jstz`) sends JACers' date and times.\n"
                  f"►`{p}jsyoutube` or (`{p}jsyt`) sends Just a chat... YouTubers' channels and videos.",
            inline=False)
        embed_ext2.set_footer(text=f"Requested by {ctx.author.name} | Page 3/3", icon_url=ctx.author.avatar_url)

        if section <= 0:
            raise commands.BadArgument
        else:
            embed = discord.Embed(
                title="Just a bot...",
                description="**Just a bot...** is a personal Discord bot developed for playing around with "
                            "creating a bot for [Just a chat...](https://aminoapps.com/c/conlang-conscript/home/) "
                            "users' servers.",
                colour=COLOUR)

            await ctx.send(embed=embed)
            if section == 1:
                await ctx.send(embed=embed_ext0)
            elif section == 2:
                await ctx.send(embed=embed_ext1)
            elif section == 3:
                await ctx.send(embed=embed_ext2)
            else:
                raise commands.BadArgument

    # Exception Handler.

    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please insert a positive integer less or equal to 3.")


def setup(bot):
    bot.add_cog(Help(bot))
