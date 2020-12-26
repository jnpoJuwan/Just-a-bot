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
    #  FIXME: Add a prettier `!help` command.
    @commands.command(aliases=["commands", "information"])
    async def info(self, ctx, section=1):
        """Send an embed with the Just a bot...'s information and a section of its commands."""
        with open("configs/prefixes.json") as pf:
            p = json.load(pf)[str(ctx.message.guild.id)]

        if section <= 0:
            raise commands.BadArgument
        else:
            async with ctx.typing():
                embed = discord.Embed(
                    title="Just a bot...",
                    description="**Just a bot...** is a personal Discord bot developed for playing around with "
                                "creating a bot for [Just a chat...](https://aminoapps.com/c/conlang-conscript/home/) "
                                "users' servers.",
                    colour=COLOUR)

            if section == 1:
                async with ctx.typing():
                    embed_ext = discord.Embed(
                        title="Miscellaneous Commands (1/3)",
                        description=f"""►`{p}info [section]` sends information regarding this bot.
                                    ►`{p}8ball [question]` asks the *Magic 8-Ball* for answers.
                                    ►`{p}cbt` sends the Wikipedia summary and page for Cock and Ball Torture.
                                    ►`{p}choose [list]` randomly chooses an item of choice.
                                    ►`{p}choose_map` (or `{p}map`) randomly chooses an Among Us map.
                                    ►`{p}direct_message` (or `!dm`) direct messages you a nice message.
                                    ►`{p}echo [message]` (or `{p}say [message]`) echoes the message.
                                    ►`{p}penis [@member]` sends a member's dick length.
                                    ►`{p}spam [amount] [message]` spams a message an given amount of times.
                                    ►`{p}umlaut [message]` sënds yöür sëntëncë wïth ümläüts.
                                    ►`{p}hello` Hi!
                                    ►`{p}ping` Pong.""",
                        colour=COLOUR)
                    embed_ext.add_field(name="Action Commands",
                                        value=f"""►`{p}kiss [member]` kisses the member.
                                              ►`{p}fuck [member]` fucks the member's arse.
                                              ►`{p}poke [member]` pokes the member.
                                              ►`{p}slap [member]` slaps the member in the face.""")
            elif section == 2:
                async with ctx.typing():
                    embed_ext = discord.Embed(
                        title="Administration Commands (2/3)",
                        description=f"""►`{p}ban <@member> (reason)` bans the member.
                                    ►`{p}change_prefix [prefix]` changes the server's prefix.
                                    ►`{p}kick <@member> (reason)` kicks the member.
                                    ►`{p}logout` logouts the bot.
                                    ►`{p}purge [amount]` (or `{p}clear (num)`) purges the amount of messages.
                                    ►`{p}unban <user_id>` unbans the user.""",
                        colour=COLOUR)
            elif section == 3:
                async with ctx.typing():
                    embed_ext = discord.Embed(
                        title="Utility Commands (3/3)",
                        description=f"""►`{p}coin_flip [amount]` flips a coin an amount of times.\
                                    ►`{p}eval [command]` evaluates the Python code.
                                    ►`{p}get_prefix` sends the server's prefix.
                                    ►`{p}length [message]` sends the message's length.
                                    ►`{p}poll [question]` creates a poll for a question.
                                    ►`{p}random` sends a fractional random number between 0 and 1.
                                    ►`{p}roll [die] [amount]` rolls a die of a input number an amount of times.
                                    ►`{p}source_code` sends the link to the bot's GitHub repository.
                                    ►`{p}words [message]` sends the number of words in the message.""",
                        colour=COLOUR)
                    embed_ext.add_field(
                        name="Information Commands",
                        value=f"""►`{p}member [@member]` sends the member's information.
                              ►`{p}pfp [@member]` sends the member's profile picture.
                              ►`{p}server` sends the server's information.""",
                        inline=False)
                    embed_ext.add_field(
                        name="Just a chat... Commands",
                        value=f"""►`{p}jsdocs` (or `{p}jsd`) sends Just some documents....
                              ►`{p}jsguidelines` (or `{p}jsg`) sends Amino Just some guidelines.
                              ►`{p}jstimezones` (or `{p}jstz`) sends JACers' date and times.
                              ►`{p}jsyoutube` or (`{p}jsyt`) sends Just a chat... YouTubers' channels and videos.""",
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
