import random

import discord
from discord.ext import commands


class Actions(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def bonk(self, ctx, member: discord.Member = None):
		"""Bonks someone."""
		if not member:
			await ctx.send('You didn\'t bonk anyone.')
		elif member == ctx.author:
			await ctx.send('You bonked yourself.')
		elif member == self.bot.user:
			await ctx.send('You bonked me.')
		else:
			await ctx.send(f'You bonked {member.display_name} to horny jail.')
			await member.send(f'{ctx.author.name} bonk you to horny jail.')

	@commands.command()
	async def cuddle(self, ctx, member: discord.Member = None):
		"""Cuddles someone."""
		if not member:
			await ctx.send('You cuddled your pillow, since you\'re alone and lonely.')
		elif member == ctx.author:
			await ctx.send('You cuddled yourself.')
		elif member == self.bot.user:
			await ctx.send('You cuddled me.')
		else:
			await ctx.send(f'You cuddled {member.display_name}.')
			await member.send(f'{ctx.author.name} cuddled you.')

	@commands.command(aliases=["cri"])
	async def cry(self, ctx):
		"""Cries."""
		image = discord.File(open('bot/data/cry.jpg', 'rb'))
		await ctx.send('<:cat_cry:814925690528333885>', file=image)

	@commands.command(aliases=['ejaculate', 'cream', 'jizz', 'nut', 'sperm', 'splooge'])
	async def cum(self, ctx, member: discord.Member = None):
		"""Cums or creams someone."""
		if not member:
			await ctx.send('Oopsie-doopsie! You cummed all over yourself!')
		if member == ctx.author:
			await ctx.send('You creamed yourself.')
		elif member == self.bot.user:
			await ctx.send('You want to c-cum inside my tiny robot bussy, master? o//w//o')
		else:
			await ctx.send(
				(f'You creamed {member.display_name}\' little þussy. '
				 'You\'re under arrest to horny jail.' if member.display_name.lower().endswith('s')
				 else f'You creamed {member.display_name}\'s little þussy. '
				      'You\'re under arrest to horny jail.')
			)
			await member.send(f'{ctx.author.name} creamed you.')

	@commands.command(aliases=['dnace'])
	async def dance(self, ctx, member: discord.Member = None):
		"""Dance with someone."""
		if not member or member == ctx.author:
			await ctx.send('You danced with yourself.')
		elif member == self.bot.user:
			await ctx.send('You danced with me.')
		else:
			await ctx.send(f'You danced with {member.display_name}.')
			await member.send(f'{ctx.author.name} danced with you.')

	@commands.command()
	async def frost(self, ctx, member: discord.Member = None):
		"""Frosts someone."""
		if not member:
			image = discord.File(open('bot/data/frost.png', 'rb'))
			await ctx.send(file=image)
		elif member == ctx.author:
			await ctx.send('You frosted yourself like a birthday cake.')
		elif member == self.bot.user:
			await ctx.send('You frosted me like a birthday cake.')
		else:
			await ctx.send(f'You frosted {member.display_name} like a birthday cake.')
			await member.send(f'{ctx.author.name} frosted you like a birthday cake.')

	@commands.command(aliases=['fuq', 'fwk', 'destroy', 'sex'])
	async def fuck(self, ctx, member: discord.Member = None):
		"""Fucks someone."""
		if not member:
			await ctx.send('You fucked your pillow, since you\'re alone and lonely, and officially became PD6.')
		elif member == ctx.author:
			await ctx.send('You self-fucked.')
		elif member == self.bot.user:
			await ctx.send('You fucked my tiny robot þussy. 😳 👉👈')
		else:
			await ctx.send(
				(f'You fucked {member.display_name}\' þussy. '
				 'You\'re under arrest to horny jail.' if member.display_name.lower().endswith('s')
				 else f'You fucked {member.display_name}\'s þussy. You\'re under arrest to horny jail.')
			)
			await member.send(f'{ctx.author.name} fucked your þussy.')

	@commands.command(aliases=['hand_hold', 'hold_hands'])
	async def hold_hand(self, ctx, member: discord.Member = None):
		"""Holds hands with someone."""
		if not member or member == ctx.author:
			await ctx.send('You held your own hand, since you\'re alone and lonely.')
		elif member == self.bot.user:
			await ctx.send('You held my robot hand.')
		else:
			await ctx.send(f'You committed pre-marital hand holding with {member.display_name}.')
			await member.send(f'{ctx.author.name} fucking destroyed your fragile asshole.')

	@commands.command()
	async def hug(self, ctx, member: discord.Member = None):
		"""Hugs someone."""
		if not member:
			await ctx.send('You hugged your pillow, since you\'re alone and lonely.')
		elif member == ctx.author:
			await ctx.send('You hugged yourself.')
		elif member == self.bot.user:
			await ctx.send('You hugged me. I appreciate it. 🥺')
		else:
			await ctx.send(f'You hugged {member.display_name}.')
			await member.send(f'{ctx.author.name} hugged you.')

	@commands.command(aliases=['assassinate', 'murder', 'slaughter'])
	async def kill(self, ctx, member: discord.Member = None):
		"""Brutally kills someone."""
		if not member:
			await ctx.send('You didn\'t killed anyone.')
		elif member == ctx.author:
			await ctx.send('<:cat_cry:814925690528333885> <:hug:810945431005560843>')
		elif member == self.bot.user:
			await ctx.send('But m-master... \\*is brutally killed\\*')
		else:
			await ctx.send(f'You have murdered {member.display_name}. You\'re now on MAGNVS\' wanted list.')
			await member.send(f'{ctx.author.name} killed you.')

	@commands.command()
	async def kiss(self, ctx, member: discord.Member = None):
		"""Kisses someone."""
		if not member:
			await ctx.send('You kissed your pillow, since you\'re alone and lonely.')
		elif member == ctx.author:
			await ctx.send('You kissed yourself.')
		elif member == self.bot.user:
			await ctx.send('You kissed me, master. 🥺')
		else:
			await ctx.send(f'You kissed {member.display_name}. 😳 👉👈')
			await member.send(f'{ctx.author.name} kissed you.')

	@commands.command()
	async def love(self, ctx):
		"""Love ❤️ 💕."""
		image = discord.File(open('bot/data/love.jpg', 'rb'))
		await ctx.send('❤️ 💕', file=image)

	@commands.command()
	async def moan(self, ctx):
		"""Moans."""
		image = discord.File(open('bot/data/moan.png', 'rb'))
		await ctx.send('And this guy moaned at least this loud.', file=image)

	@commands.command(aliases=['headpat'])
	async def pat(self, ctx, member: discord.Member = None):
		"""Pats someone on the head."""
		if not member:
			await ctx.send('You patted your pillow, since you\'re alone and lonely.')
		elif member == ctx.author:
			await ctx.send('You patted yourself.')
		elif member == self.bot.user:
			await ctx.send('You patted me. 🥺')
		else:
			await ctx.send(f'You patted {member.display_name} on the head.')
			await member.send(f'{ctx.author.name} patted you on the head.')

	@commands.command()
	async def poke(self, ctx, member: discord.Member = None):
		"""Pokes someone."""
		if not member:
			await ctx.send('You poked your pillow, since you\'re alone and lonely.')
		elif member == ctx.author:
			await ctx.send('You poked yourself.')
		elif member == self.bot.user:
			await ctx.send('You poked me.')
		else:
			await ctx.send(f'You poked {member.display_name}.')
			await member.send(f'{ctx.author.name} poked you.')

	@commands.command()
	async def punish(self, ctx, member: discord.Member = None):
		"""Punishes someone."""
		if not member:
			await ctx.send('You didn\'t punish anyone.')
		elif member == ctx.author:
			await ctx.send('You punished yourself.')
		elif member == self.bot.user:
			await ctx.send('You punished me.')
		else:
			await ctx.send(f'You punished {member.display_name}.')
			await member.send(f'{ctx.author.name} punished you.')

	@commands.command()
	async def reject(self, ctx, member: discord.Member = None):
		"""Rejects someone."""
		if not member:
			await ctx.send('You didn\'t reject anyone.')
		elif member == ctx.author:
			await ctx.send('You rejected yourself. <:noooooooo:809935851052072980>')
		elif member == self.bot.user:
			await ctx.send('You rejected me. <:noooooooo:809935851052072980>')
		else:
			await ctx.send(f'You rejected {ctx.author.display_name}.')
			await member.send(f'{ctx.author.name} rejected you.')

	@commands.command()
	async def scream(self, ctx):
		"""Screams."""
		file = open('bot/data/scream.jpg', 'rb')
		image = discord.File(file)
		await ctx.send(file=image)

	@commands.command()
	async def shoot(self, ctx, member: discord.Member = None):
		"""Shoots someone."""
		if not member:
			await ctx.send('You didn\'t shoot anyone.')
		elif member == ctx.author:
			await ctx.send('<:cat_cry:814925690528333885> <:hug:810945431005560843>')
		elif member == self.bot.user:
			await ctx.send('\\*gets shot\\*.')
		else:
			await ctx.send(f'You shot {member.display_name}.')
			await member.send(f'{ctx.author.name} shot you.')

	@commands.command()
	async def shy_hug(self, ctx, member: discord.Member = None):
		"""Shyly hugs someone."""
		if not member:
			await ctx.send('You hugged your pillow, since you\'re alone and lonely.')
		elif member == ctx.author:
			await ctx.send('You hugged yourself.')
		elif member == self.bot.user:
			await ctx.send('You hugged me. I appreciate it. 🥺')
		else:
			await ctx.send(f'You hugged {member.display_name}. 😳 👉👈')
			await member.send(f'{ctx.author.name} hugged you.')

	@commands.command()
	async def slap(self, ctx, member: discord.Member = None):
		"""Slaps someone's face or their thicc, juicy arse."""
		# XXX: Probably not the best solution.
		choices = [
			('You facepalmed.',
			 'You slapped me.',
			 f'You slapped {member.display_name}.',
			 f'{ctx.author.name} slapped you.'),

			('You slapped your own thicc, juicy arse',
			 'You slapped my arse.',
			 (f'You slapped {member.display_name}\' thicc, juicy arse.' if member.display_name.lower().endswith('s')
			  else f'You slapped {member.display_name}\'s thicc, juicy arse.'),
			 f'{ctx.author.name} slapped your thicc, juicy arse.')
		]

		output = random.choice(choices)
		if not member or member == ctx.author:
			await ctx.send(output[0])
		elif member == self.bot.user:
			await ctx.send(output[1])
		else:
			await ctx.send(output[2])
			await member.send(output[3])

	@commands.command()
	async def stab(self, ctx, member: discord.Member = None):
		"""Stabs someone."""
		if not member:
			await ctx.send('You didn\'t stab anyone.')
		elif member == ctx.author:
			await ctx.send('<:cat_cry:814925690528333885> <:hug:810945431005560843>')
		elif member == self.bot.user:
			await ctx.send('\\*gets stabbed 23 times\\* Et tu, dominus? \\*dies\\*.')
		else:
			await ctx.send(f'You brutally stabbed {member.display_name}.')
			await member.send(f'{ctx.author.name} stabbed your heart.')

	@commands.command(aliases=['suq'])
	async def suck(self, ctx, member: discord.Member = None):
		"""Sucks someone off."""
		if not member or member == ctx.author:
			image = discord.File(open('bot/data/suck.png', 'rb'))
			await ctx.send(file=image)
		elif member == self.bot.user:
			await ctx.send('You sucked my tiny cock.')
		else:
			await ctx.send(f'You sucked {member.display_name}. You\'re under arrest to horny jail.')
			await member.send(f'{ctx.author.name} sucked you.')

	@bonk.error
	@cuddle.error
	@cum.error
	@dance.error
	@fuck.error
	@hold_hand.error
	@hug.error
	@kill.error
	@kiss.error
	@poke.error
	@punish.error
	@reject.error
	@shoot.error
	@slap.error
	@stab.error
	@suck.error
	async def member_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send('Please @mention a member.')


def setup(bot):
	bot.add_cog(Actions(bot))
