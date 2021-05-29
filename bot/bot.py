from pathlib import Path

import discord
import traceback
from discord.ext import commands

from .configs.configs import OWNER_ID
from .utils import exceptions
from .utils.constants import DEFAULT_PREFIX, SPAM_LIMIT


# CRED: @Rapptz (https://github.com/Rapptz/RoboDanny/blob/rewrite/bot.py#L44)
def _prefix_callable(bot, message):
    _id = bot.user.id
    base = [f'<@!{_id}> ', f'<@{_id}> ', DEFAULT_PREFIX]
    return base


class JustABot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=_prefix_callable, case_insensitive=True, owner_id=OWNER_ID)
        self.was_ready_once = False

    # CRED: @Tortoise-Community (https://github.com/Tortoise-Community/Tortoise-BOT/blob/master/bot/bot.py#L65)
    def load_extensions(self):
        for extension_path in Path('bot/cogs').glob('*.py'):
            extension_name = extension_path.stem

            dotted_path = f'bot.cogs.{extension_name}'

            try:
                self.load_extension(dotted_path)
            except Exception as e:
                traceback_msg = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
                print(f'Failed to load cog {dotted_path}. Traceback:\n{"".join(traceback_msg)}')

    async def on_ready(self):
        print(f'Logged in as @{self.user.name}.')

        if not self.was_ready_once:
            await self.on_first_ready()
            self.was_ready_once = True

    async def on_first_ready(self):
        self.load_extensions()
        await self.change_presence(activity=discord.Game(name=f'{DEFAULT_PREFIX}help | {len(self.guilds)} servers'))

    @staticmethod
    async def on_connect():
        print("Connection to Discord established.")

    @staticmethod
    async def on_disconnect():
        print("Connection to Discord lost.")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please enter all required arguments.')
        elif isinstance(error, commands.CheckFailure):
            await ctx.send('You don\'t have permission to use that command.')
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'You\'re using this command too much. Try again in {round(error.retry_after)} seconds.')
        elif isinstance(error, exceptions.SpamError):
            await ctx.send(f'The amount can\'t exceed {SPAM_LIMIT}.')

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)
