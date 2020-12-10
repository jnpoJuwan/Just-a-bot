import json
import os

import discord
from discord.ext import commands

from just_a_bot.cogs.spam import SPAM_LIMIT
from just_a_bot.utils import exceptions


COGS = [file for file in os.listdir("cogs") if file.endswith(".py") and not file.startswith("__")]
DEFAULT_PREFIX = "!"


def _prefix_callable(_bot, message):
    _id = bot.user.id
    base = [f'<@!{_id}> ', f'<@{_id}> ']
    if message.guild is None:
        base.append(DEFAULT_PREFIX)
    else:
        with open("configs/prefixes.json") as pf:
            prefixes = json.load(pf)
            base.append(prefixes[str(message.guild.id)])
    return base

class JustABot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=_prefix_callable,
            case_insensitive=True,
            owner_id=488828457703309313
        )
        self.default_prefix = DEFAULT_PREFIX

    # Events.

    async def on_ready(self):
        activity = discord.Game(name="with Juwan's mental state.")
        await self.change_presence(activity=activity)
        print(f"INFO: Logged on as @{bot.user.name}.")

    async def on_command_error(self, ctx, error):
        # Server Errors
        if isinstance(error, exceptions.ServerNotFoundError):
            await ctx.send("You're not allowed to use this command in this server.")
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send("You're not allowed to use this commands in private messages.")
        # Command Errors
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Sorry. I can't find that command.")
        if isinstance(error, commands.DisabledCommand):
            await ctx.send("Sorry. This command is disabled, hence it can't be used.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please insert all required arguments.")
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You're not allowed to use this command.")
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You're using command too much. Try again in {round(error.retry_after)} seconds.")
        # else:
        #     await ctx.send("Sorry. An unidentified error has occurred.")

    async def on_guild_join(self, guild):
        with open("configs/prefixes.json") as pf:
            prefixes = json.load(pf)
        with open("configs/prefixes.json", "w") as pf:
            prefixes[str(guild.id)] = self.default_prefix
            json.dump(prefixes, pf, indent=2)

    async def on_guild_remove(self, guild):
        with open("configs/prefixes.json") as pf:
            prefixes = json.load(pf)
        with open("configs/prefixes.json", "w") as pf:
            prefixes.pop(str(guild.id))
            json.dump(prefixes, pf, indent=2)

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)


bot = JustABot()

if __name__ == "__main__":
    for cog in COGS:
        bot.load_extension(f"cogs.{cog[:-3]}")

    with open("configs/secrets.json") as cf:
        token = json.load(cf)["token"]
    bot.run(token)
