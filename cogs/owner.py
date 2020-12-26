import os

from discord.ext import commands

from ._utils.constants import COGS
from ._utils import checks


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def load(self, ctx, module):
        """Load a module."""
        try:
            self.bot.load_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send(f"`{module}` has been loaded.")

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def unload(self, ctx, module):
        """Unload a module."""
        try:
            self.bot.unload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send(f"`{module}` has been unloaded.")

    @commands.group(hidden=True)
    @checks.is_bot_owner()
    async def reload(self, ctx, module):
        """Reload a module."""
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send(f"`{module}` has been reloaded.")

    @reload.command(name="all", hidden=True)
    async def reload_all(self, ctx):
        """Reload all cogs."""
        async with ctx.typing():
            for module in COGS:
                await self.bot.reload_extension(module)
        await ctx.send("All cogs have been reloaded.")

    # Exception Handling.

    @load.error
    @unload.error
    @reload.error
    async def load_cogs_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Sorry. I can't find that cog.")


def setup(bot):
    bot.add_cog(Owner(bot))
