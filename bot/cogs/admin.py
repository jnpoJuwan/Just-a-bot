import json

import discord
from discord.ext import commands

from ..utils import checks
from ..utils.constants import DEFAULT_PREFIX


class Admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.guild_only()
	@checks.is_admin()
	async def ban(self, ctx, member: discord.Member, *, reason='No specific reason.'):
		"""Bans the member."""
		try:
			await member.ban(reason=reason)
		except discord.Forbidden:
			await ctx.send(f'Unable to ban {member.display_name}.')
		else:
			await ctx.send(f'{member.name} was successfully banned.')

	@commands.command()
	@commands.guild_only()
	@checks.is_admin()
	async def kick(self, ctx, member: discord.Member, *, reason='No specific reason.'):
		"""Kicks the member."""
		try:
			await member.kick(reason=reason)
		except discord.Forbidden:
			await ctx.send(f'Unable to kick {member.display_name}.')
		else:
			await ctx.send(f'{member.name} was successfully kicked.')

	@ban.error
	@kick.error
	async def kickban_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send('Please @mention a member.')

	@commands.command(aliases=['change_prefix'])
	@commands.guild_only()
	@checks.is_admin()
	async def set_prefix(self, ctx, prefix=None):
		"""Sets the server's prefix."""
		prefix = prefix or DEFAULT_PREFIX
		prefixes = json.load(open('bot/configs/prefixes.json'))

		prefixes[str(ctx.guild.id)] = prefix
		with open('bot/configs/prefixes.json', 'w') as f:
			json.dump(prefixes, f, indent=2, sort_keys=True)

		await ctx.send(f'The server\'s prefix has been changed to `{prefix}`.')

	@commands.command()
	@commands.guild_only()
	@checks.is_admin()
	async def unban(self, ctx, user_id: int = None):
		"""Unbans the user."""
		if user_id is None:
			raise commands.BadArgument

		user = self.bot.get_user(user_id=user_id)
		await ctx.guild.unban(user)
		await ctx.send(f'{user} was unbanned by {ctx.author.mention}.')

	@unban.error
	async def unban_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send(
				'Please insert a valid user ID.\nHow to get an user ID:'
				'https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-'
			)


def setup(bot):
	bot.add_cog(Admin(bot))
