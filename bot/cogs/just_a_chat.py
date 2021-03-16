import asyncio
import datetime

import discord
from discord.ext import commands
from pytz import timezone, utc

from ..utils.constants import COLOUR, ARROW_TO_BEGINNING, LEFT_ARROW, DELETE_EMOJI, RIGHT_ARROW, ARROW_TO_END, \
	PAGINATION_EMOJI


class JustAChat(commands.Cog, name='Just a chat...'):
	def __init__(self, bot):
		self.bot = bot

	# GLOSS: 'js' means 'Just some', not 'JavaScript'.

	@commands.command(aliases=['jacdocs', 'jsd', 'just_some_documents'])
	async def jsdocs(self, ctx):
		"""Sends Just some documents...."""
		docs_dict = {
			'Just some documents...': {
				'Just a bot...':
					'https://github.com/jnpoJuwan/Just-a-bot',
				'Just a map...':
					'https://goo.gl/maps/Z3VDj5JkwpVrDUSd7',
				'Just some (fuck-able) ages...':
					'https://docs.google.com/document/d/1xeAlaHXVZ4PfFm_BrOuAxXrO-0SBZZZvZndCpI0rkDc/edit?usp=sharing',
				'Just some guidelines...':
					'https://docs.google.com/document/d/1NAH6GZNC0UNFHdBmAd0u9U5keGhAgnxY-vqiRaATL8c/edit?usp=sharing',
				'Just some history...':
					'https://docs.google.com/document/d/1g6-8aTLQ4ct6SR88GJA1hrQkIgB5_tU1CQGh4s3I9cM/edit?usp=sharing',
				'Just some languages...':
					'https://docs.google.com/document/d/1ay2Ue2D6teOY4XjO-tqThffzYgwV-WHKaxJlZCU4DDA/edit?usp=sharing',
				'Just some penises...':
					'https://docs.google.com/document/d/1gUoTqg4uzdSG_0eqoERcbMBFBrWdIEw6IBy_L3OrRnQ/edit?usp=sharing',
				'Just some stories...':
					'https://docs.google.com/document/d/1EGwg2vBL6VHaXK0B0u1mEXGV8SE9w6Xr1axlN8rB-Ic/edit?usp=sharing',
			},

			'Just some documents... (Continuation)': {
				'Just some units of measurement...':
					'https://docs.google.com/document/d/1Zk1unIM76WaBvOh1ew04nEbSPxH1Gq54M3Tu4Znj05A/edit?usp=sharing',
				'(Extended) International Phonetic Alphabet':
					'https://docs.google.com/spreadsheets/d/1Rx8ui5eug2Qk__B9IQkxVxFkdZaxbDkgGI2xNicqbtM'
					'/edit?usp=sharing'
			},

			'*Boyfriends* Extra Chapters': {
				'Extra Chapter 01 (Goth x Nerd)':
					'https://drive.google.com/file/d/1qzXIDXNiVZw3Kra0lzSJBwb911ROyOLA/view?usp=drivesdk ',
				'Extra Chapter 02 (Jock x Prep)':
					'https://drive.google.com/file/d/1wdU-XGUCcNXAm1QmpRDxa_vZMgljiQok/view?usp=drivesdk'
			},
		}

		pages = [{k: v} for k, v in docs_dict.items()]

		# CRED: @Tortoise-Community
		# (https://github.com/Tortoise-Community/Tortoise-BOT/blob/master/bot/utils/paginator.py)
		i = 0

		def page_counter():
			return f'Page {i + 1}/{len(pages)}'

		def get_page_title():
			for heading, _ in pages[i].items():
				return heading

		def get_page_content():
			for _, content in pages[i].items():
				docs_links = [f'• **[{text}]({url})**' for text, url in content.items()]
				return '\n'.join(docs_links)

		embed = discord.Embed(title=get_page_title(), description=get_page_content(), colour=COLOUR)
		embed.set_footer(text=f'Requested by {ctx.author.display_name} | {page_counter()}',
		                 icon_url=ctx.author.avatar_url)
		message = await ctx.send(embed=embed)

		for emoji in PAGINATION_EMOJI:
			await message.add_reaction(emoji)

		async def update_message():
			embed.title = get_page_title()
			embed.description = get_page_content()
			embed.set_footer(text=f'Requested by {ctx.author.display_name} | {page_counter()}',
			                 icon_url=ctx.author.avatar_url)
			await message.edit(embed=embed)

		async def clear_all_reactions():
			try:
				await message.clear_reactions()
			except discord.HTTPException:
				# Silently ignore if no permission to remove reaction.
				pass

		def check(reaction_, member):
			return (
					str(reaction_) in PAGINATION_EMOJI and
					member.id == ctx.author.id and
					reaction_.message.id == message.id
			)

		while True:
			try:
				reaction, user = await self.bot.wait_for('reaction_add', timeout=300, check=check)
			except asyncio.TimeoutError:
				await clear_all_reactions()
				break

			if str(reaction) == ARROW_TO_BEGINNING:
				await message.remove_reaction(ARROW_TO_BEGINNING, ctx.author)
				if i > 0:
					i = 0
					await update_message()
			elif str(reaction) == LEFT_ARROW:
				await message.remove_reaction(LEFT_ARROW, ctx.author)
				if i > 0:
					i -= 1
					await update_message()
			elif str(reaction) == DELETE_EMOJI:
				return await message.delete()
			elif str(reaction) == RIGHT_ARROW:
				await message.remove_reaction(RIGHT_ARROW, ctx.author)
				if i < len(pages) - 1:
					i += 1
					await update_message()
			elif str(reaction) == ARROW_TO_END:
				await message.remove_reaction(ARROW_TO_END, ctx.author)
				if i < len(pages) - 1:
					i = len(pages) - 1
					await update_message()

	@commands.command(aliases=['jactimezones', 'jactz', 'jstz'])
	async def jstimezones(self, ctx):
		"""Sends Just a chat... users' time zones."""
		message = await ctx.send('Calculating times...')

		await ctx.trigger_typing()
		dt = datetime.datetime.now(tz=utc)
		tz_dict = {
			'🇲🇽 Mexico (Pacific)': timezone('Mexico/BajaSur'),
			'🇺🇸 US (Mountain)': timezone('US/Mountain'),
			'🇲🇽 Mexico (Central)': timezone('Mexico/General'),
			'🇺🇸 US (Central)': timezone('US/Central'),
			'🇺🇸 US (Eastern)': timezone('US/Eastern'),
			'🇵🇾 Paraguay': timezone('America/Asuncion'),
			'🇧🇷 Brazil (Brasília)': timezone('Brazil/East'),
			'🇪🇺 Europe (Western)': timezone('Europe/London'),
			'🇪🇺 Europe (Central)': timezone('Europe/Berlin'),
			'🇪🇺 Europe (Eastern)': timezone('Europe/Athens'),
			'🇦🇪 United Arab Emirates': timezone('Asia/Dubai'),
			'🇰🇷 South Korea': timezone('Asia/Seoul'),
		}

		embed = discord.Embed(title='Just some time zones...', colour=COLOUR)
		for k, v in tz_dict.items():
			embed.add_field(name=k, value=str(dt.astimezone(v).strftime('%A, %B %d **%H:%M** UTC%z')))

		embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
		await message.edit(embed=embed)

	@commands.command(aliases=['jacyoutube', 'jacyt', 'jsyt'])
	async def jsyoutube(self, ctx):
		"""Send some Just a chat... users' YouTube channels."""
		channels_dict = {
			'Aurora': 'https://www.youtube.com/channel/UCmDE7oQp2wzTLxd7lc4mA9A',
			'D\'ignoranza': 'https://www.youtube.com/channel/UCI4ZJ0QmSokr6ctUfURqm5A',
			'Dr. IPA': 'https://www.youtube.com/channel/UCfPYxsZHRBaW24q3pb9oOnA',
			'Dracheneks': 'https://www.youtube.com/channel/UCiaOA8yjnuZX5wUqmlRDUuA',
			'MAGNVS': 'https://www.youtube.com/channel/UC2AcuqQOPxH6pkbJs-xm_Qw',
			'PD6': 'https://www.youtube.com/channel/UCuAsPOh-qA7wakswF6ioo4g',
		}

		embed = discord.Embed(name='Just some YouTube channels...', colour=COLOUR)
		for k, v in channels_dict.items():
			embed.add_field(name=k, value=v)

		embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command(aliases=['jacguidelines', 'jsg'])
	@commands.cooldown(1, 60.0, commands.BucketType.user)
	async def jsguidelines(self, ctx, paginator='on'):
		"""
		Sends the Just a chat... guidelines from Amino.

		The paginator can be turned either on or off.
		"""
		# SEE: https://docs.google.com/document/d/1NAH6GZNC0UNFHdBmAd0u9U5keGhAgnxY-vqiRaATL8c/edit?usp=sharing

		if paginator not in ['off', 'on']:
			raise commands.BadArgument

		file = open('bot/data/languages.md', encoding='utf-8')
		lines = file.readlines()
		pages = [{}]

		for line in lines[1:]:
			if len(pages[-1]) >= 24 or line.startswith('# '):
				pages.append({})

			if line.startswith('## '):
				heading_line = lines.index(line)
				page_content = ''.join(lines[heading_line + 1: heading_line + 4])[:-1]
				# Find the last dictionary and append this section into it.
				dict_indices = [i for i, v in enumerate(pages) if isinstance(v, dict)]
				pages[dict_indices[-1]][line[3:-1]] = page_content

		if paginator == 'off':
			embed = discord.Embed(title='Just some guidelines...', colour=COLOUR)
			for page in pages[:-1]:
				for k, v in page.items():
					embed.add_field(name=k, value=v)
				await ctx.send(embed=embed)
				embed.clear_fields()

			# Only the last embed needs a footer.
			for k, v in pages[-1].items():
				embed.add_field(name=k, value=v)
			embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		else:
			i = 0

			def page_counter():
				return f'Page {i + 1}/{len(pages)}'

			embed = discord.Embed(title='Just some guidelines...', colour=COLOUR)
			for k, v in pages[i].items():
				embed.add_field(name=k, value=v)
			embed.set_footer(text=f'Requested by {ctx.author.display_name} | {page_counter()}',
			                 icon_url=ctx.author.avatar_url)
			message = await ctx.send(embed=embed)

			for emoji in PAGINATION_EMOJI:
				await message.add_reaction(emoji)

			async def update_message():
				embed.clear_fields()
				for _k, _v in pages[i].items():
					embed.add_field(name=_k, value=_v)
				embed.set_footer(text=f'Requested by {ctx.author.display_name} | {page_counter()}',
				                 icon_url=ctx.author.avatar_url)
				await message.edit(embed=embed)

			async def clear_all_reactions():
				try:
					await message.clear_reactions()
				except discord.HTTPException:
					# Silently ignore if no permission to remove reaction.
					pass

			def check(reaction_, member):
				return (
						str(reaction_) in PAGINATION_EMOJI and
						member.id == ctx.author.id and
						reaction_.message.id == message.id
				)

			while True:
				try:
					reaction, user = await self.bot.wait_for('reaction_add', timeout=300, check=check)
				except asyncio.TimeoutError:
					await clear_all_reactions()
					break

				if str(reaction) == ARROW_TO_BEGINNING:
					await message.remove_reaction(ARROW_TO_BEGINNING, ctx.author)
					if i > 0:
						i = 0
						await update_message()
				elif str(reaction) == LEFT_ARROW:
					await message.remove_reaction(LEFT_ARROW, ctx.author)
					if i > 0:
						i -= 1
						await update_message()
				elif str(reaction) == DELETE_EMOJI:
					return await message.delete()
				elif str(reaction) == RIGHT_ARROW:
					await message.remove_reaction(RIGHT_ARROW, ctx.author)
					if i < len(pages) - 1:
						i += 1
						await update_message()
				elif str(reaction) == ARROW_TO_END:
					await message.remove_reaction(ARROW_TO_END, ctx.author)
					if i < len(pages) - 1:
						i = len(pages) - 1
						await update_message()

	@jsguidelines.error
	async def jsguidelines_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send('The paginator must be turned either on or off.')


def setup(bot):
	bot.add_cog(JustAChat(bot))
