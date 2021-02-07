from discord.ext import commands


class ServerNotFoundError(commands.CheckFailure):
    pass


class SpamError(commands.CommandError):
    pass
