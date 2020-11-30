import random

import discord
from discord.ext import commands

from .misc import SPAM_LIMIT


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["len"])
    async def length(self, ctx, *, message):
        """Send the length of the message's content"""
        await ctx.send(f"**{len(message)}**")

    @commands.command()
    async def random(self, ctx):
        """Send a random number in the range [0, 1) or [0, 1] depending on rounding."""
        await ctx.send(f"**{random.random()}**")

    @commands.command(aliases=["dice", "randint"])
    async def roll(self, ctx, *, b=20, amount=1):
        """Send a random integer in range [1, b], including both end points, an amount of times."""
        if b < 1:
            raise commands.BadArgument
        else:
            if amount > SPAM_LIMIT:
                await ctx.send("That's too much. The amount can't exceed {SPAM_LIMIT}.")
            else:
                for i in range(amount):
                    await ctx.send(f"**{random.randint(1, b)}**")

    # Exception Handling

    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please input a positive integer (Use `!random` for rationals).")


def setup(bot):
    bot.add_cog(Utils(bot))
