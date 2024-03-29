import io
import textwrap
import traceback
from contextlib import redirect_stdout
from pathlib import Path

from discord.ext import commands

from ..utils import checks


class Owner(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='quit')
    @checks.is_bot_owner()
    async def _quit(self, ctx):
        """Logout from Discord."""
        await ctx.send('Quiting bot...')
        await self.bot.logout()

    @staticmethod
    def cleanup_code(content):
        # Remove ```py\n```.
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # Remove `foo`.
        return content.strip('` \n')

    # CRED: @Rapptz (https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py)
    @commands.command(name='eval', pass_context=True)
    @checks.is_bot_owner()
    async def eval_(self, ctx, *, body: str):
        """Evaluates Python code."""
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()
        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except:
            value = stdout.getvalue()
            await ctx.send(f'```\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```\n{value}{ret}\n```')

    # CRED: @Rapptz (https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py)
    @commands.command()
    @checks.is_bot_owner()
    async def load(self, ctx, module):
        """Loads a module."""
        try:
            self.bot.load_extension(module)
        except Exception as e:
            traceback_msg = ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
            await ctx.send(f'Failed to load cog {module}. Traceback:\n```{traceback_msg}```')
        else:
            await ctx.send(f'`{module}` has been loaded.')

    @commands.command()
    @checks.is_bot_owner()
    async def unload(self, ctx, module):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            traceback_msg = ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
            await ctx.send(f'Failed to load cog {module}. Traceback:\n```{traceback_msg}```')
        else:
            await ctx.send(f'`{module}` has been unloaded.')

    @commands.command()
    @checks.is_bot_owner()
    async def reload(self, ctx, module):
        """Reloads a module."""
        try:
            self.bot.reload_extension(module)
        except Exception as e:
            traceback_msg = ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
            await ctx.send(f'Failed to load cog {module}. Traceback:\n```{traceback_msg}```')
        else:
            await ctx.send(f'`{module}` has been reloaded.')

    @commands.command()
    @checks.is_bot_owner()
    async def reload_all(self, ctx):
        """Reloads all extensions."""
        content = 'Reloading modules...'
        message = await ctx.send('Reloading modules...')

        for extension_path in Path('bot/cogs').glob('*.py'):
            extension_name = extension_path.stem

            dotted_path = f'bot.cogs.{extension_name}'

            try:
                self.bot.reload_extension(dotted_path)
                content += f'\nReloaded `{dotted_path}`.'
                await message.edit(content=content)
            except Exception as e:
                traceback_msg = ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
                await ctx.send(f'Failed to load cog {dotted_path}. Traceback:\n```{traceback_msg}```')

        content += '\nSuccessfully reloaded all extensions.'
        await message.edit(content=content)


def setup(bot):
    bot.add_cog(Owner(bot))
