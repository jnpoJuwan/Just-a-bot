import traceback
from pathlib import Path

from discord.ext import commands

from ..utils import checks


class Owner(commands.Cog, command_attrs=dict(hidden=True)):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='quit', aliases=['die', 'logout', 'sleep'])
	@checks.is_bot_owner()
	async def _quit(self, ctx):
		"""Logout from Discord."""
		await ctx.send('**change da world**\n**my final message. Goodb ye**')
		await self.bot.logout()

	# CREDIT: @Rapptz (https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py#L116)
	@commands.command()
	@checks.is_bot_owner()
	async def load(self, ctx, module):
		"""Loads a module."""
		module = 'bot.cogs.' + module
		try:
			self.bot.load_extension(module)
		except Exception as e:
			await ctx.send(f'**{e.__class__.__name__}:** {e}')
		else:
			await ctx.send(f'`{module}` has been loaded.')

	@commands.command()
	@checks.is_bot_owner()
	async def unload(self, ctx, module):
		"""Unloads a module."""
		module = 'bot.cogs.' + module
		try:
			self.bot.unload_extension(module)
		except Exception as e:
			await ctx.send(f'**{e.__class__.__name__}:** {e}')
		else:
			await ctx.send(f'`{module}` has been unloaded.')

	@commands.command()
	@checks.is_bot_owner()
	async def reload(self, ctx, module):
		"""Reloads a module."""
		module = 'bot.cogs.' + module
		try:
			self.bot.reload_extension(module)
		except Exception as e:
			await ctx.send(f'**{e.__class__.__name__}:** {e}')
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
				traceback_msg = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
				await ctx.send(f"Failed to load cog {dotted_path}\nTraceback: {traceback_msg}")

		content += '\nSuccessfully reloaded all extensions.'
		await message.edit(content=content)


def setup(bot):
	bot.add_cog(Owner(bot))
