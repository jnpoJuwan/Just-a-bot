import os

from discord.ext import commands

from ..configs.constants import COGS
from ..utils import checks


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def load(self, ctx, cog=None):
        """Load a cog."""
        if not cog:
            for file in COGS:
                async with ctx.typing():
                    self.bot.load_extension(f"cogs.{file.lower()[:-3]}")
                await ctx.send(f"**`cogs.{file.lower()[:-3]}` has been loaded.**")
        else:
            file = f"{cog.lower()}.py"
            if not os.path.exists(f"cogs/{file}"):
                raise commands.BadArgument
            elif file.endswith(".py") and not file.startswith("__"):
                async with ctx.typing():
                    self.bot.load_extension(f"cogs.{file[:-3]}")
                await ctx.send(f"**`cogs.{file[:-3]}` has been loaded.**")

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def unload(self, ctx, cog=None):
        """Unload a cog."""
        if not cog:
            for file in COGS:
                async with ctx.typing():
                    self.bot.unload_extension(f"cogs.{file.lower()[:-3]}")
                await ctx.send(f"**`cogs.{file.lower()[:-3]}` has been unloaded.**")
        else:
            file = f"{cog.lower()}.py"
            if not os.path.exists(f"cogs/{file}"):
                raise commands.BadArgument
            elif file.endswith(".py") and not file.startswith("__"):
                async with ctx.typing():
                    self.bot.unload_extension(f"cogs.{file[:-3]}")
                await ctx.send(f"**`cogs.{file[:-3]}` has been unloaded.**")

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def reload(self, ctx, cog=None):
        """Reload either a cog or all cogs."""
        if not cog:
            for file in COGS:
                async with ctx.typing():
                    self.bot.reload_extension(f"cogs.{file.lower()[:-3]}")
                await ctx.send(f"**`cogs.{file.lower()[:-3]}` has been reloaded.**")
        else:
            file = f"{cog.lower()}.py"
            if not os.path.exists(f"cogs/{file}"):
                raise commands.BadArgument
            elif file.endswith(".py") and not file.startswith("__"):
                async with ctx.typing():
                    self.bot.reload_extension(f"cogs.{file[:-3]}")
                await ctx.send(f"**`cogs.{file[:-3]}` has been reloaded.**")

    # Exception Handling.

    @load.error
    @unload.error
    @reload.error
    async def load_cogs_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Sorry. I can't find that cog.")


def setup(bot):
    bot.add_cog(Owner(bot))
