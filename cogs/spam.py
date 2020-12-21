from discord.ext import commands

from ._utils.constants import SPAM_LIMIT
from ._utils import exceptions

# This module is separate from the 'fun' module
# for the bot owners to be able to unload the spam alone, and not break other commands.

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def spam(self, ctx, amount=5, *, message="spam"):
        """Spam a message an amount of times."""
        if amount <= SPAM_LIMIT:
            for _ in range(amount):
                await ctx.send(message)
        else:
            raise exceptions.SpamError

    # Exception Handling.

    @spam.error
    async def spam_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Insert the spam amount and, optionally, a message, in this order.")


def setup(bot):
    bot.add_cog(Spam(bot))
