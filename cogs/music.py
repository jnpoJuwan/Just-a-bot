import discord
from discord.ext import commands


class Music(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Fuck off, MΛGNVS. I can't to understand this at all.


def setup(bot):
	bot.add_cog(Music(bot))
