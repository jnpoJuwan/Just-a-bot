from discord.ext import commands

from .misc import SPAM_LIMIT

# This module is separate from the 'misc' module
# for the developer to be able to unload the spam alone, and not break other commands.


class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def spam(self, ctx, amount=5, *, message="spam"):
        """Spam a message an amount of times."""
        if amount > SPAM_LIMIT:
            await ctx.send(f"That's too much spam, bitch. The amount can't exceed {SPAM_LIMIT} in amount")
        else:
            for i in range(amount):
                await ctx.send(message)

    # Exception Handling.

    @spam.error
    async def spam_error(self, ctx, error):
        if isinstance(error, ValueError):
            await ctx.send("Insert the spam amount and, optionally, a message, in this order.")


def setup(bot):
    bot.add_cog(Spam(bot))
