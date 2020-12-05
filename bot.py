import json
import os

import discord
from discord.ext import commands


COGS = [file for file in os.listdir("./cogs") if file.endswith(".py") and not file.startswith("__")]
DEFAULT_PREFIX = "!"


class JustABot(commands.Bot):
    @staticmethod
    def __prefix_callable(_bot, message):
        user_id = bot.user.id
        base = [f'<@!{user_id}> ', f'<@{user_id}> ']
        if message.guild is None:
            base.append(DEFAULT_PREFIX)
        else:
            with open("configs/prefixes.json") as pf:
                prefixes = json.load(pf)
                base.append(prefixes[str(message.guild.id)])
        return base

    def __init__(self):
        super().__init__(
            command_prefix=self.__prefix_callable,
            case_insensitive=True,
            owner_id=488828457703309313
        )
        self.default_prefix = DEFAULT_PREFIX

    async def on_ready(self):
        activity = discord.Game(name="with Juwan's mental state.")
        await self.change_presence(activity=activity)
        print(f"INFO: Logged on as @{bot.user.name}.")


bot = JustABot()

if __name__ == "__main__":
    for cog in COGS:
        bot.load_extension(f"cogs.{cog[:-3]}")

    with open("configs/secrets.json") as cf:
        token = json.load(cf)["token"]
    bot.run(token)
