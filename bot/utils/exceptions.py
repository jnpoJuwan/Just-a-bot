from discord.ext import commands


class SpamError(commands.CommandError):
    pass


class UnknownError(commands.CommandError):
    pass
