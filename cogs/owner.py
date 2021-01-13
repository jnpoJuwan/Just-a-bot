import json

from discord.ext import commands

from ._utils import checks


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'INFO: {__name__} is ready.')

    @commands.command()
    @checks.is_bot_owner()
    async def add_server(self, ctx):
        guild = ctx.guild

        with open('configs/jsservers.json') as f:
            servers = json.load(f)
        with open('configs/jsservers.json', 'w') as f:
            json.dump(servers.append(guild.id), f, indent=2, sort_keys=True)

        await ctx.send(f'{guild.name} has been added to the list of Just a chat... servers.')

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


def setup(bot):
    bot.add_cog(Owner(bot))
