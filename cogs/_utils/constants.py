import os

import discord

COGS = [f'cogs.{module[:-3]}' for module in os.listdir('cogs') if module.endswith('.py')
        and not module.startswith('_')]
COLOUR = discord.Colour(0x8b0000)
DEFAULT_PREFIX = '?'
SPAM_LIMIT = 25
