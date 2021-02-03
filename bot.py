import json

import discord
from discord.ext import commands

from cogs._utils import exceptions
# HACK: I don't know why, but importing from cogs._utils.constants breaks *something* (maybe in my IDE),
# so instead I have to copy the constants from there to configs.configs instead.
from configs.configs import DEFAULT_PREFIX, OWNER_ID, SPAM_LIMIT


# CREDIT: Rapptz (GitHub [https://github.com/Rapptz/RoboDanny/blob/rewrite/bot.py#L44])
def _prefix_callable(bot, message):
	_id = bot.user.id
	base = [f'<@!{_id}> ', f'<@{_id}> ']
	if message.guild is None:
		base.append(DEFAULT_PREFIX)
	else:
		prefixes = json.load(open('configs/prefixes.json'))
		base.append(prefixes[str(message.guild.id)])
	return base


class JustABot(commands.Bot):
	def __init__(self):
		super().__init__(
			command_prefix=_prefix_callable,
			case_insensitive=True,
			owner_id=OWNER_ID
		)
		self.default_prefix = DEFAULT_PREFIX

	# Events.

	async def on_ready(self):
		activity = discord.Game(name='with Juwan\'s mental state.')
		await self.change_presence(activity=activity)
		print(f'INFO: Logged on as @{self.user.name}.')

	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			# await ctx.send('Sorry. I can\'t find that command.')
			await ctx.send('Sowwy! Oopsie-doopsie! We made a fucky wucky! '
			               'We couldn\'t locate that commandy-wandy that you wanted! OwO!')
		elif isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Please insert all required arguments.')
		elif isinstance(error, commands.CheckFailure):
			await ctx.send('You don\'t have permission to use that command.')
		elif isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f'You\'re using this command too much. Try again in {round(error.retry_after)} seconds.')
		elif isinstance(error, exceptions.SpamError):
			await ctx.send(f'That\'s too much spam. The amount can\'t exceed {SPAM_LIMIT}.')

	async def on_guild_join(self, guild):
		file = 'configs/prefixes.json'
		prefixes = json.load(open(file))
		with open('configs/prefixes.json', 'w') as f:
			prefixes[str(guild.id)] = self.default_prefix
			json.dump(prefixes, f, indent=2)

	async def on_guild_remove(self, guild):
		file = 'configs/prefixes.json'
		prefixes = json.load(open(file))
		with open('configs/prefixes.json', 'w') as f:
			prefixes.pop(str(guild.id))
			json.dump(prefixes, f, indent=2, sort_keys=True)

	async def on_member_join(self, member):
		if member.guild.id == 750863262911954964:
			role = discord.utils.get(member.guild.roles, name='Just a member...')
			await member.add_roles(role)

	async def on_message(self, message):
		if message.author.bot:
			return
		await self.process_commands(message)
