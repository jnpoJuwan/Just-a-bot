from discord.ext import commands

from ._utils import checks
from ._utils.constants import COGS


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='quit', aliases=['die', 'logout', 'sleep'])
    @checks.is_bot_owner()
    async def _quit(self, ctx):
        """Logout from Discord."""
        await ctx.send('**change da world**\n**my final message. Goodb ye**')
        await self.bot.logout()

    # CREDIT: @Rapptz (GitHub [https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py#L116])
    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def load(self, ctx, module):
        """Load a module."""
        try:
            self.bot.load_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'**{e.__class__.__name__}:** {e}')
        else:
            await ctx.send(f'`{module}` has been loaded.')

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def unload(self, ctx, module):
        """Unload a module."""
        try:
            self.bot.unload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'**{e.__class__.__name__}:** {e}')
        else:
            await ctx.send(f'`{module}` has been unloaded.')

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def reload(self, ctx, module):
        """Reload a module."""
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'**{e.__class__.__name__}:** {e}')
        else:
            await ctx.send(f'`{module}` has been reloaded.')

    @commands.command(hidden=True)
    @checks.is_bot_owner()
    async def reload_all(self, ctx):
        """Reload all extensions."""
        msg = await ctx.send('Reloading modules...')
        for module in COGS:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
            await msg.edit(content=f'`{module}` has been reloaded.')

        await msg.edit(content='All extensions have been successfully reloaded.')


def setup(bot):
    bot.add_cog(Owner(bot))
