from discord.ext import commands

from ._utils import checks


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # CREDIT: @Rapptz (GitHub [https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py#L116])
    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def load(self, ctx, module):
        """Load a module."""
        try:
            self.bot.load_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f"**{e.__class__.__name__}:** {e}")
        else:
            await ctx.send(f"`{module}` has been loaded.")

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def unload(self, ctx, module):
        """Unload a module."""
        try:
            self.bot.unload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f"**{e.__class__.__name__}:** {e}")
        else:
            await ctx.send(f"`{module}` has been unloaded.")

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def reload(self, ctx, module):
        """Reload a module."""
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f"**{e.__class__.__name__}:** {e}")
        else:
            await ctx.send(f"`{module}` has been reloaded.")


def setup(bot):
    bot.add_cog(Owner(bot))
