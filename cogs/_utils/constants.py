import os

import discord

COLOUR = discord.Colour(0x8b0000)
COGS = [module for module in os.listdir("cogs") if module.endswith(".py") and not module.startswith("_")]
DEFAULT_PREFIX = "!"
SPAM_LIMIT = 25
