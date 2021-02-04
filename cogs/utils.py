import io
import json
import textwrap
import traceback
import random
from contextlib import redirect_stdout

import discord
from discord.ext import commands

from ._utils import exceptions
from ._utils.constants import SPAM_LIMIT


class Utils(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def choose(self, ctx, *args):
		"""Chooses a random item from the list."""
		map(lambda x: x.strip(','), args)
		await ctx.send(f'**{random.choice(args)}**')

	def cleanup_code(self, content):
		# Remove ```py\n```.
		if content.startswith('```') and content.endswith('```'):
			return '\n'.join(content.split('\n')[1:-1])

		# Remove `foo`.
		return content.strip('` \n')

	# CREDIT: @Rapptz (GitHub [https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py#L216])
	@commands.command(name='eval', pass_context=True)
	async def _eval(self, ctx, *, body: str):
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
			return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

		func = env['func']
		try:
			with redirect_stdout(stdout):
				ret = await func()
		except:
			value = stdout.getvalue()
			await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
		else:
			value = stdout.getvalue()

			if ret is None:
				if value:
					await ctx.send(f'```py\n{value}\n```')
			else:
				self._last_result = ret
				await ctx.send(f'```py\n{value}{ret}\n```')

	@commands.command(aliases=['coin_flip', 'heads', 'tails'])
	async def flip_coin(self, ctx, amount=1):
		"""Flips coins."""
		if amount >= SPAM_LIMIT:
			raise exceptions.SpamError

		for _ in range(amount):
			await ctx.send(f'**{random.choice(["Heads", "Tails"])}**')

	@commands.command(aliases=['prefix'])
	async def get_prefix(self, ctx):
		"""Gets the server's prefix."""
		file = open('configs/prefixes.json')
		p = json.load(file)[str(ctx.message.guild.id)]
		await ctx.send(f'This server\'s prefix is `{p}`.')

	@commands.command(aliases=['dice', 'randint'])
	async def roll(self, ctx, *, b: int = 20, amount: int = 1):
		"""Rolls the given number-sided dice."""
		if b < 1:
			await ctx.send('Please enter a positive integer.')
			return
		if amount >= SPAM_LIMIT:
			raise exceptions.SpamError

		for _ in range(amount):
			await ctx.send(f'**{random.randint(1, b)}**')

	@roll.error
	async def roll_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send('Please enter a positive integer.')


def setup(bot):
	bot.add_cog(Utils(bot))
