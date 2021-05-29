from discord.ext import commands

from ..utils import checks


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['clear', 'delete'])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    @checks.is_mod()
    async def purge(self, ctx, amount=0):
        """Purges the amount of messages."""
        await ctx.message.delete()
        limit = 200
        if amount > limit:
            await ctx.send(f'The amount can\'t exceed {limit} messages.', delete_after=2.5)
            return

        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Successfully purged {amount} message(s).', delete_after=2.5)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please enter an amount of messages.')


def setup(bot):
    bot.add_cog(Mod(bot))
