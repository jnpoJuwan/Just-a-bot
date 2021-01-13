import json
import random

import discord
import wikipedia
from discord.ext import commands

from ._utils.constants import COLOUR


class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f'INFO: {__name__} is ready.')

	@commands.command(name='8ball', aliases=['8-ball'])
	async def _8ball(self, ctx, *, question='???'):
		"""Choose a random answer from the Magic 8-Ball."""
		# SEE: https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
		outcomes = ('It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.',
		            'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
		            'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
		            'Cannot predict now.', 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.',
		            'My sources say no.', 'Outlook not so good.', 'Very doubtful.')
		await ctx.send(f'> {question}\n**{random.choice(outcomes)}**')

	@commands.command(aliases=['cock_and_ball_torture'])
	async def cbt(self, ctx):
		"""Send an embed with the summary for the Wikipedia page of 'Cock and ball torture'."""
		# SEE: https://en.wikipedia.org/wiki/Cock_and_ball_torture
		async with ctx.typing():
			embed = discord.Embed(title='Cock and ball torture',
			                      url='https://en.wikipedia.org/wiki/Cock_and_ball_torture',
			                      description=wikipedia.summary('Cock_and_ball_torture'), colour=COLOUR)
			embed.set_footer(text=f'Requested by {ctx.author.display_name} | Summary by Wikipedia',
			                 icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command(aliases=['map', 'random_map'])
	async def choose_map(self, ctx):
		"""Choose a random Among Us map."""
		outcomes = 'The Skeld', 'MIRA HQ', 'Polus'
		await ctx.send(f'You should play in **{random.choice(outcomes)}.**')

	@commands.command(aliases=['say'])
	async def echo(self, ctx, *, text='echo'):
		"""Echo the user's input-message."""
		await ctx.send(text)

	@commands.command(hidden=True, aliases=['fuckyou', 'f*ck_you'])
	async def fuck_you(self, ctx):
		"""Respond to 'fuck you'."""
		await ctx.send('Fuck my robot body yourself, you fucking coward :rage:.')

	@commands.command(aliases=['hey', 'hi'])
	async def hello(self, ctx):
		"""Greet the author."""
		greetings = ['G\'day!', 'Good afternoon!', 'Good evening!', 'Good morning!', 'Hello!', 'Hey!', 'Hey, you!',
		             'Hey, you. You\'re finally awake.', '*Hey~* ;)', 'Hi!', 'How are you?', 'Howdy!', 'What\'s up?']
		await ctx.send(random.choice(greetings))

	@commands.command(aliases=['cock', 'dick'])
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def penis(self, ctx, member: discord.Member = None):
		"""Send a random penis size between [0, 30] cm."""
		member = member or ctx.author
		n = random.randint(0, 30)
		if member == self.bot.get_user(320325816712167426):  # @PD6#1510
			n = 0

		if n < 5:
			await ctx.send(f'{member.mention}\'s micropenis is {n} cm long: **8{"=" * n}D**')
		elif n < 20:
			await ctx.send(f'{member.mention}\'s penis is {n} cm long: **8{"=" * n}D**')
		else:
			await ctx.send(f'{member.mention}\'s hard monster cock is {n} cm long: **8{"=" * n}D**')

	@commands.command()
	async def ping(self, ctx):
		"""Send 'pong'."""
		await ctx.send('pong')

	@commands.command()
	async def poll(self, ctx, *, question):
		"""Create a basic poll."""
		embed = discord.Embed(title='Poll', description=question, colour=COLOUR)
		embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)
		message = await ctx.send(embed=embed)
		await message.add_reaction('👍')
		await message.add_reaction('👎')
		await message.add_reaction('🤷')

	@commands.command(aliases=['pang', 'peng', 'pung', 'pyng', 'pwng'])
	async def pong(self, ctx):
		"""Send 'ping' (sike)."""
		await ctx.send('No! This isn\'t how you\'re supposed to play the game.')

	@commands.command(hidden=True)
	async def spam(self, ctx):
		with open('configs/prefixes.json') as f:
			p = json.load(f)[str(ctx.message.guild.id)]
		await ctx.send(f'I\'ve already told you `{p}spam` isn\'t an available command anymore.')

	@commands.command(aliases=['diaeresis'])
	async def umlaut(self, ctx, *, text='None'):
		"""Send the given text with umlauted vowels."""
		for vowel in 'aeiouwyAEIOUWY':
			text = text.replace(vowel, vowel + '\u0308')
		await ctx.send(text)

	# Exception Handling.

	@penis.error
	async def member_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send('Please @mention a member.')


def setup(bot):
	bot.add_cog(Fun(bot))
