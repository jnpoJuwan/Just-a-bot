import os

import discord


COLOUR = discord.Colour(0x8b0000)
COGS = [file for file in os.listdir("cogs") if file.endswith(".py") and not file.startswith("__")]
DEFAULT_PREFIX = "!"
SPAM_LIMIT = 25
