import random

import discord
from discord.ext import commands


class Actions(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def bonk(self, ctx, member: discord.Member = None):
		"""Bonks someone."""
		if not member or member == ctx.author:
			await ctx.send('You cuddled your pillow, since you\'re alone and lonely.')
		elif member == self.bot.user:
			await ctx.send('You bonked me.')
		else:
			await ctx.send(f'You bonked {member.display_name} to horny jail.')
			await member.send(f'{ctx.author.name} bonk you to horny jail.')

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
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
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def cry(self, ctx):
		"""Cries."""
		image = discord.File(open('bot/data/cry.jpg', 'rb'))
		await ctx.send(file=image)

	@commands.command(aliases=['ejaculate', 'cream', 'jizz', 'nut', 'sperm', 'splooge'])
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def cum(self, ctx, member: discord.Member = None):
		"""Cums or creams someone."""
		if not member:
			await ctx.send('Oopsie-doopsie! You cummed all over yourself!')
		if member == ctx.author:
			image = discord.File(open('bot/data/cream.png', 'rb'))
			await ctx.send(file=image)
		elif member == self.bot.user:
			await ctx.send('Y-you want to c-cum inside my tiny robot bussy, master? o///o')
		else:
			await ctx.send(
				(f'You creamed {member.display_name}\' little bussy. '
				 'You\'re under arrest to horny jail.' if member.display_name.lower().endswith('s')
				 else f'You creamed {member.display_name}\'s little bussy. '
				      'You\'re under arrest to horny jail.')
			)
			await member.send(f'{ctx.author.name} creamed you.')

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def dance(self, ctx, member: discord.Member = None):
		"""Dance with someone."""
		if not member or member == ctx.author:
			await ctx.send('You danced alone.')
		elif member == self.bot.user:
			await ctx.send('You danced with me.')
		else:
			await ctx.send(f'You danced with {member.display_name}.')
			await member.send(f'{ctx.author.name} danced with you.')

	@commands.command(aliases=['fuq'])
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def fuck(self, ctx, member: discord.Member = None):
		"""Fucks someone."""
		if not member:
			await ctx.send('You fucked your pillow, since you\'re alone and lonely, '
			               'and officially became PD6.')
		elif member == ctx.author:
			await ctx.send('You self-fucked.')
		elif member == self.bot.user:
			await ctx.send('You fucking destroyed my fragile robot bussy.')
		else:
			await ctx.send(
				(f'You destroyed {member.display_name}\' fragile asshole. '
				 'You\'re under arrest to horny jail.' if member.display_name.lower().endswith('s')
				 else f'You destroyed {member.display_name}\'s fragile asshole. '
				      'You\'re under arrest to horny jail.')
			)
			await member.send(f'{ctx.author.name} fucking destroyed your fragile asshole.')

	@commands.command(aliases=['hand_hold', 'hold_hands'])
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def hold_hand(self, ctx, member: discord.Member = None):
		"""Holds hands with someone."""
		if not member or member == ctx.author:
			await ctx.send('You held your own hand.')
		elif member == self.bot.user:
			await ctx.send('You held my robot hand.')
		else:
			await ctx.send(f'You committed pre-marital hand holding with {member.display_name}.')
			await member.send(f'{ctx.author.name} fucking destroyed your fragile asshole.')

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def hug(self, ctx, member: discord.Member = None):
		"""Hugs someone."""
		if not member:
			await ctx.send('You hugged your pillow, since you\'re alone and lonely.')
		elif member == ctx.author:
			await ctx.send('You hugged yourself.')
		elif member == self.bot.user:
			await ctx.send('You hugged me. I appreciate it.')
		else:
			await ctx.send(f'You hugged {member.display_name}.')
			await member.send(f'{ctx.author.name} hugged you.')

	@commands.command(aliases=['assassinate', 'murder', 'slaughter'])
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def kill(self, ctx, member: discord.Member = None):
		"""Brutally kills someone."""
		if not member:
			await ctx.send('You didn\'t killed anyone.')
		elif member == ctx.author:
			await ctx.send('Do you want to talk about this, master?')
		elif member == self.bot.user:
			await ctx.send('But m-master... \\*is brutally killed\\*')
		else:
			await ctx.send(f'You have murdered {member.display_name}. You\'re now on the Magnvs\' wanted list.')
			await member.send(f'{ctx.author.name} killed you.')

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def kiss(self, ctx, member: discord.Member = None):
		"""Kisses someone."""
		if not member:
			await ctx.send('You kissed your pillow, since you\'re lonely.')
		elif member == ctx.author:
			await ctx.send('You kissed yourself.')
		elif member == self.bot.user:
			await ctx.send('You kissed me, master. 🥺')
		else:
			await ctx.send(f'You kissed {member.display_name}. 😳 👉👈')
			await member.send(f'{ctx.author.name} kissed you.')

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def love(self, ctx):
		"""Love ❤️ 💕."""
		image = discord.File(open('bot/data/love.jpg', 'rb'))
		await ctx.send('❤️ 💕', file=image)

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def moan(self, ctx):
		"""Moans."""
		image = discord.File(open('bot/data/moan.png', 'rb'))
		await ctx.send('And this guy moaned at least this loud.', file=image)

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def poke(self, ctx, member: discord.Member = None):
		"""Pokes the given member."""
		if not member or member == ctx.author:
			await ctx.send('You poked yourself.')
		elif member == self.bot.user:
			await ctx.send('You poked me.')
		else:
			await ctx.send(f'You poked {member.display_name}.')
			await member.send(f'{ctx.author.name} poked you.')

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def reject(self, ctx, member: discord.Member = None):
		"""Reject someone."""
		if not member or member == ctx.author:
			await ctx.send('You rejected yourself. <:noooooooo:809935851052072980>')
		elif member == self.bot.user:
			await ctx.send('You rejected me. <:noooooooo:809935851052072980>')
		else:
			await ctx.send(f'Ew. Get away from {ctx.author.display_name}, {member.display_name}.')
			await member.send(f'{ctx.author.name} rejected you.')

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def scream(self, ctx):
		"""Screams."""
		file = open('bot/data/scream.jpg', 'rb')
		image = discord.File(file)
		await ctx.send(file=image)

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def shoot(self, ctx, member: discord.Member = None):
		"""Shoot someone."""
		if not member:
			await ctx.send('You didn\'t shoot anyone.')
		elif member == ctx.author:
			await ctx.send('Do you want to talk about this, master?')
		elif member == self.bot.user:
			await ctx.send('\\*gets shot\\*.')
		else:
			await ctx.send(f'You shot {member.display_name}.')
			await member.send(f'{ctx.author.name} shot you.')

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def slap(self, ctx, member: discord.Member = None):
		"""Slaps someone's face or juicy arse."""
		# HACK: Probably not the best solution, but it's good enough.
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
		if not member:
			await ctx.send('It hurt itself in its confusion!')
		elif member == ctx.author:
			await ctx.send(output[0])
		elif member == self.bot.user:
			await ctx.send(output[1])
		else:
			await ctx.send(output[2])
			await member.send(output[3])

	@commands.command()
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def stab(self, ctx, member: discord.Member = None):
		"""Stab someone."""
		if not member:
			await ctx.send('You didn\'t stab anyone.')
		elif member == ctx.author:
			await ctx.send('Are you OK, master?')
		elif member == self.bot.user:
			await ctx.send('\\*gets stabbed 23 times\\* Et tu, dominus? \\*dies\\*.')
		else:
			await ctx.send(f'You brutally stabbed {member.display_name}.')
			await member.send(f'{ctx.author.name} stabbed your heart.')

	@commands.command(aliases=['suq'])
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	async def suck(self, ctx, member: discord.Member = None):
		"""Sucks someone off."""
		if not member or member == ctx.author:
			image = discord.File(open('bot/data/suck.png', 'rb'))
			await ctx.send(file=image)
		elif member == self.bot.user:
			await ctx.send('You sucked my tiny cock.')
		elif member.id == 567488628003962880:  # Dr. IPA#3047
			await ctx.send(f'You suqqed {member.display_name}. You\'re under arrest to horny jail.')
			await member.send(f'{ctx.author.name} suqqed you.')
		else:
			await ctx.send(f'You sucked {member.display_name}. You\'re under arrest to horny jail.')
			await member.send(f'{ctx.author.name} sucked you.')

	@cuddle.error
	@cum.error
	@fuck.error
	@hold_hand.error
	@hug.error
	@kill.error
	@kiss.error
	@poke.error
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
