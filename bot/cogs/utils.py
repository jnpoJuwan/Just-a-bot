import io
import json
import textwrap
import traceback
import random
from contextlib import redirect_stdout

import discord
from async_cse import Search
from discord.ext import commands

from ..configs.configs import GOOGLE_API_KEY
from ..utils import exceptions
from ..utils.constants import COLOUR, SPAM_LIMIT
from ..utils.paginator import ListPaginator


class Utils(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.google_client = Search(GOOGLE_API_KEY)

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

	# CRED: @Rapptz (https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py#L216)
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
		file = open('bot/configs/prefixes.json')
		p = json.load(file)[str(ctx.message.guild.id)]
		await ctx.send(f'This server\'s prefix is `{p}`.')

	# Siúlann An Troll#1517 challenged me to make this.
	# CRED: @Tortoise-Community (https://github.com/Tortoise-Community/Tortoise-BOT/blob/master/bot/cogs/utility.py#L19)
	# CAVEAT: Google's Custom Search JSON API provides only 100 search queries per day for free.
	@commands.command()
	async def google(self, ctx, *, query='query'):
		"""Searches Google for a query."""
		page_list = []

		await ctx.trigger_typing()
		results = await self.google_client.search(query)
		i = 1

		for result in results:
			embed = discord.Embed(title=result.title, description=result.description, url=result.url, colour=COLOUR)
			embed.set_thumbnail(url=result.image_url)
			# TODO: Should be handled by paginator. <@Tortoise-Community>
			embed.set_footer(text=f'Requested by {ctx.author.display_name} | Page {i}/{len(results)} | {query}',
			                 icon_url=ctx.author.avatar_url)

			page_list.append(embed)
			i += 1

		paginator = ListPaginator(ctx, page_list)
		await paginator.start()

	@commands.command()
	async def poll(self, ctx, *, question):
		"""Creates a basic yes/no poll."""
		embed = discord.Embed(title='Poll', description=question, colour=COLOUR)
		embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
		message = await ctx.send(embed=embed)
		await message.add_reaction('👍')
		await message.add_reaction('👎')
		await message.add_reaction('🤷')

	@commands.command(aliases=['poll_num'])
	async def pollnum(self, ctx, *, question):
		"""Creates a basic poll with numbers."""
		embed = discord.Embed(title='Poll', description=question, colour=COLOUR)
		embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
		message = await ctx.send(embed=embed)
		await message.add_reaction('1️⃣')
		await message.add_reaction('2️⃣')
		await message.add_reaction('3️⃣')

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
