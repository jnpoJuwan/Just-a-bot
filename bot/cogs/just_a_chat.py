import asyncio
import datetime

import discord
from discord.ext import commands
from pytz import timezone, utc

from ..utils import checks
from ..utils.constants import COLOUR
from ..utils.paginator import FIRST_ARROW, LEFT_ARROW, DELETE_EMOJI, RIGHT_ARROW, LAST_ARROW, PAGINATION_EMOJI


class JustAChat(commands.Cog, name='Just a chat...'):
	def __init__(self, bot):
		self.bot = bot

	# GLOSS: 'js' means 'Just some', not 'JavaScript'.

	@commands.command(aliases=['jsd', 'just_some_documents'])
	async def jsdocs(self, ctx):
		"""Sends Just some documents...."""
		docs_values = {
			'Just a bot...': 'https://github.com/jnpoJuwan/Just-a-bot',
			'Just a map...': 'https://goo.gl/maps/Z3VDj5JkwpVrDUSd7',
			'Just some (fuck-able) ages...':
				'https://docs.google.com/document/d/1xeAlaHXVZ4PfFm_BrOuAxXrO-0SBZZZvZndCpI0rkDc/edit?usp=sharing',
			'Just some guidelines...':
				'https://docs.google.com/document/d/1NAH6GZNC0UNFHdBmAd0u9U5keGhAgnxY-vqiRaATL8c/edit?usp=sharing',
			'Just some penises...':
				'https://docs.google.com/document/d/1gUoTqg4uzdSG_0eqoERcbMBFBrWdIEw6IBy_L3OrRnQ/edit?usp=sharing',
			'Just some stories...':
				'https://docs.google.com/document/d/1EGwg2vBL6VHaXK0B0u1mEXGV8SE9w6Xr1axlN8rB-Ic/edit?usp=sharing',
			'Just some units of measurement...':
				'https://docs.google.com/document/d/1Zk1unIM76WaBvOh1ew04nEbSPxH1Gq54M3Tu4Znj05A/edit?usp=sharing',
			'(Extended) International Phonetic Alphabet':
				'https://docs.google.com/spreadsheets/d/1Rx8ui5eug2Qk__B9IQkxVxFkdZaxbDkgGI2xNicqbtM'
				'/edit?usp=sharing',
		}

		embed = discord.Embed(title='Just some documents...', colour=COLOUR)
		for k, v in docs_values.items():
			embed.add_field(name=k, value=v, inline=False)
		embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command(aliases=['jstz'])
	async def jstimezones(self, ctx):
		"""Sends Just a chat... users' time zones."""
		message = await ctx.send('Calculating time zones...')

		# ctx.typing() is used, since this command takes an *extremely* long time.
		async with ctx.typing():
			dt = datetime.datetime.now(tz=utc)
			fmt = '%A, %B %d **%H:%M** UTC%z'
			tz_values = {
				':flag_mx: Mexico (Pacific)': timezone('Mexico/BajaSur'),
				':flag_um: US (Mountain)': timezone('US/Mountain'),
				':flag_mx: Mexico (Central)': timezone('Mexico/General'),
				':flag_us: US (Central)': timezone('US/Central'),
				':flag_um: US (Eastern)': timezone('US/Eastern'),
				':flag_py: Paraguay': timezone('America/Asuncion'),
				':flag_br: Brazil (Brasília)': timezone('Brazil/East'),
				':flag_eu: Europe (Western)': timezone('Europe/London'),
				':flag_eu: Europe (Central)': timezone('Europe/Berlin'),
				':flag_eu: Europe (Eastern)': timezone('Europe/Athens'),
				':flag_ae: United Arab Emirates': timezone('Asia/Dubai'),
				':flag_kr: South Korea': timezone('Asia/Seoul'),
			}

			embed = discord.Embed(title='Just some time zones...', colour=COLOUR)
			for k, v in tz_values.items():
				embed.add_field(name=k, value=str(dt.astimezone(v).strftime(fmt)))
			embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
		await message.edit(embed=embed)

	@commands.command(aliases=['jsyt'])
	async def jsyoutube(self, ctx):
		"""Send some Just a chat... user's YouTube channels."""
		channel_values = {
			'Aurora': 'https://www.youtube.com/channel/UCmDE7oQp2wzTLxd7lc4mA9A',
			'D\'ignoranza': 'https://www.youtube.com/channel/UCI4ZJ0QmSokr6ctUfURqm5A',
			'Dr. IPA': 'https://www.youtube.com/channel/UCfPYxsZHRBaW24q3pb9oOnA',
			'Dracheneks': 'https://www.youtube.com/channel/UCiaOA8yjnuZX5wUqmlRDUuA',
			'MAGNVS': 'https://www.youtube.com/channel/UC2AcuqQOPxH6pkbJs-xm_Qw',
			'PD6': 'https://www.youtube.com/channel/UCuAsPOh-qA7wakswF6ioo4g',
		}

		embed = discord.Embed(name='Just some channels...', colour=COLOUR)
		for k, v in channel_values.items():
			embed.add_field(name=k, value=v)
		embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command(aliases=['jsg'])
	@commands.cooldown(3, 60.0, commands.BucketType.user)
	@checks.is_mod()
	async def jsguidelines(self, ctx, paginator='off'):
		"""
		Sends the Just a chat... guidelines from Amino.

		The paginator can be turned either on or off.
		"""

		# SEE: https://docs.google.com/document/d/1NAH6GZNC0UNFHdBmAd0u9U5keGhAgnxY-vqiRaATL8c/edit?usp=sharing
		if paginator not in ['off', 'on']:
			raise commands.BadArgument

		file = open('bot/languages.md', encoding='utf-8')
		lines = file.readlines()

		pages = []
		for line in lines:
			if line.startswith('# '):
				pages.append({})
			if line.startswith('## '):
				current_line = lines.index(line)
				page_content = ''.join(lines[current_line + 1:current_line + 4])[:-1]
				dict_indices = [i for i, value in enumerate(pages) if isinstance(value, dict)]
				pages[dict_indices[-1]][line[3:-1]] = page_content

		if paginator == 'off':
			embed = discord.Embed(title='Just some guidelines...', colour=COLOUR)
			for page in pages[:-1]:
				for k, v in page.items():
					embed.add_field(name=k, value=v)
				await ctx.send(embed=embed)
				embed.clear_fields()

			for k, v in pages[-1].items():
				embed.add_field(name=k, value=v)
			embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
		else:
			# CREDIT: @Tortoise-Community
			# (https://github.com/Tortoise-Community/Tortoise-BOT/blob/master/bot/utils/paginator.py)
			page_index = 0

			def page_counter():
				return f'Page {page_index + 1}/{len(pages)}'

			embed = discord.Embed(title='Just some guidelines...', colour=COLOUR)
			for k, v in pages[page_index].items():
				embed.add_field(name=k, value=v)
			embed.set_footer(text=f'Requested by {ctx.author.display_name} | {page_counter()}',
			                 icon_url=ctx.author.avatar_url)
			message = await ctx.send(embed=embed)

			for emoji in PAGINATION_EMOJI:
				await message.add_reaction(emoji)

			async def update_message():
				embed.clear_fields()
				for k, v in pages[page_index].items():
					embed.add_field(name=k, value=v)
				embed.set_footer(text=f'Requested by {ctx.author.display_name} | {page_counter()}',
				                 icon_url=ctx.author.avatar_url)
				await message.edit(embed=embed)

			async def _remove_reaction(reaction_, author: discord.Member):
				try:
					await message.remove_reaction(reaction_, author)
				except discord.HTTPException:
					# Silently ignore if no permission to remove reaction (e.g. in DMs).
					pass

			async def clear_all_reactions():
				try:
					await message.clear_reactions()
				except discord.HTTPException:
					# Silently ignore if no permission to remove reaction.
					pass

			def react_check(reaction_, member):
				return (
						str(reaction_) in PAGINATION_EMOJI and
						member.id == ctx.author.id and
						reaction_.message.id == message.id
				)

			while True:
				try:
					reaction, user = await self.bot.wait_for('reaction_add', timeout=300, check=react_check)
				except asyncio.TimeoutError:
					await clear_all_reactions()
					break

				if str(reaction) == FIRST_ARROW:
					await _remove_reaction(FIRST_ARROW, ctx.author)
					if page_index > 0:
						page_index = 0
						await update_message()
				elif str(reaction) == LEFT_ARROW:
					await _remove_reaction(LEFT_ARROW, ctx.author)
					if page_index > 0:
						page_index -= 1
						await update_message()
				elif str(reaction) == DELETE_EMOJI:
					return await message.delete()
				elif str(reaction) == RIGHT_ARROW:
					await _remove_reaction(RIGHT_ARROW, ctx.author)
					if page_index < len(pages) - 1:
						page_index += 1
						await update_message()
				elif str(reaction) == LAST_ARROW:
					await _remove_reaction(LAST_ARROW, ctx.author)
					if page_index < len(pages) - 1:
						page_index = len(pages) - 1
						await update_message()

	@jsguidelines.error
	async def jsguidelines_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send('The paginator can be turned either on or off.')


def setup(bot):
	bot.add_cog(JustAChat(bot))
