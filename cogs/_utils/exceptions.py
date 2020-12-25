from discord.ext import commands


class MemberNotFoundError(commands.CommandError):
    pass


class ServerNotFoundError(commands.CheckFailure):
    pass


class SpamError(commands.CommandError):
    pass
