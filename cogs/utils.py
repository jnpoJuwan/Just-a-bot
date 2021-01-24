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

	@commands.Cog.listener()
	async def on_ready(self):
		print(f'INFO: {__name__} is ready.')

	@commands.command()
	async def choose(self, ctx, *args):
		"""Choose a random element from the given arguments."""
		map(lambda x: x.strip(','), args)
		await ctx.send(f'**{random.choice(args)}**')

	def cleanup_code(self, content):
		"""Automatically removes code blocks from the code."""
		# Remove ```py\n```.
		if content.startswith('```') and content.endswith('```'):
			return '\n'.join(content.split('\n')[1:-1])

		# Remove `foo`.
		return content.strip('` \n')

	# CREDIT: @Rapptz (GitHub [https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py#L216])
	@commands.command(name='eval', pass_context=True)
	async def _eval(self, ctx, *, body: str):
		"""Evaluate Python code."""
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
		"""Flip a coin of the given amount of times."""
		if amount >= SPAM_LIMIT:
			raise exceptions.SpamError

		for _ in range(amount):
			await ctx.send(f'**{random.choice(["Heads", "Tails"])}**')

	@commands.command(aliases=['prefix'])
	async def get_prefix(self, ctx):
		"""Get the guild's prefix."""
		file = open('configs/prefixes.json')
		p = json.load(file)[str(ctx.message.guild.id)]
		await ctx.send(f'This server\'s prefix is `{p}`.')

	@commands.command()
	async def random(self, ctx):
		"""Send a random number in the range [0, 1) or [0, 1] depending on rounding."""
		await ctx.send(f'**{random.random()}**')

	@commands.command(aliases=['dice', 'randint'])
	async def roll(self, ctx, *, b=20, amount=1):
		"""Send a random integer in range [1, b], including both end points, an amount of times."""
		if b < 1:
			await ctx.send('Please enter a positive integer (Use `!random` for rationals).')
			return
		if amount >= SPAM_LIMIT:
			raise exceptions.SpamError

		for _ in range(amount):
			await ctx.send(f'**{random.randint(1, b)}**')


def setup(bot):
	bot.add_cog(Utils(bot))
