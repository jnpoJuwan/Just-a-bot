import discord
from discord.ext import commands

from ..utils import checks


class Mod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@checks.is_mod()
	async def mute(self, ctx, member: discord.Member):
		"""Mutes the member."""
		await member.edit(mute=True)
		await ctx.send(f'{member.display_name} has been muted.')

	@commands.command(aliases=['clear', 'delete'])
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	@checks.is_mod()
	async def purge(self, ctx, amount=0, member: discord.Member = None):
		"""Purges the amount of messages."""
		limit = 200
		if amount > limit:
			await ctx.send(f'The amount can\'t exceed {limit} messages.')
			return

		if not member:
			await ctx.message.delete()
			await ctx.channel.purge(limit=amount)
		else:
			await ctx.message.delete()
			channel = ctx.channel
			await channel.purge(limit=amount, check=lambda message: message.author == ctx.author)
		await ctx.send(f'Successfully purged {amount} message(s).', delete_after=2.5)

	@purge.error
	async def purge_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send(
				'Please enter a positive integer and, optionally, a member whose messages you want deleted.'
			)

	@commands.command()
	@checks.is_mod()
	async def unmute(self, ctx, member: discord.Member):
		"""Unmutes the member."""
		await member.edit(mute=False)
		await ctx.send(f'{member.display_name} has been unmuted.')

	@mute.error
	@unmute.error
	async def member_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send('Please @mention a member.')


def setup(bot):
	bot.add_cog(Mod(bot))
