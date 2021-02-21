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
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		"""Bans the member."""
		if member == ctx.author:
			await ctx.send('You can\'t ban yourself.')
			return

		await member.ban(reason=reason)
		await ctx.send(f'{member.name} was banned by {ctx.author.name}.')

	@commands.command()
	@commands.guild_only()
	@checks.is_admin()
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		"""Kicks the member."""
		if member == ctx.author:
			await ctx.send('You can\'t kick yourself.')
			return

		await member.kick(reason=reason)
		await ctx.send(f'{member.name} was kicked by {ctx.author.name}.')

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
