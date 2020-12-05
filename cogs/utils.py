import json
import random

import discord
from discord.ext import commands

from just_a_bot.cogs.spam import SPAM_LIMIT


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command(aliases=["coin_flip", "heads", "tails"])
    async def flip_coin(self, ctx, amount: int = 1):
        """Flips a coin of the input amount of times."""
        for i in range(amount):
            await ctx.send(f"**{random.choice(['Heads', 'Tails'])}**")

    @commands.command()
    async def get_prefix(self, ctx):
        """Send the server's prefix."""
        with open("configs/prefixes.json") as pf:
            p = json.load(pf)[str(ctx.message.guild.id)]
        await ctx.send(f"The server's prefix is `{p}`.")

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
                await ctx.send(f"That's too much. The amount can't exceed {SPAM_LIMIT}.")
            else:
                for i in range(amount):
                    await ctx.send(f"**{random.randint(1, b)}**")

    # Exception Handling.

    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please input a positive integer (Use `!random` for rationals).")


def setup(bot):
    bot.add_cog(Utils(bot))
