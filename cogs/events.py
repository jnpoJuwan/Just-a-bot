import json

import discord
from discord.ext import commands

from just_a_bot.utils import exceptions


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.Cog.listener()
    async def on_connect(self):
        print("INFO: Connected to Discord.")

    @commands.Cog.listener()
    async def on_disconnect(self):
        print("INFO: Disconnected from Discord.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Server Errors
        if isinstance(error, exceptions.ServerNotFoundError):
            await ctx.send("You're not allowed to use this command in this server.")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send("You're not allowed to use this commands in private messages.")
        # Command Errors
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("Sorry. I can't find that command.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.author.send("Sorry. This command is disabled and can't be used.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please insert all required arguments.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("You're not allowed to use this command.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You're using command too much. Try again in {round(error.retry_after)} seconds.")
        # else:
        #     await ctx.send("Sorry. An unidentified error has occurred.")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("configs/prefixes.json") as pf:
            prefixes = json.load(pf)
        with open("configs/prefixes.json", "w") as pf:
            prefixes[str(guild.id)] = self.bot.default_prefix
            json.dump(prefixes, pf, indent=2)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("configs/prefixes.json") as pf:
            prefixes = json.load(pf)
        with open("configs/prefixes.json", "w") as pf:
            prefixes.pop(str(guild.id))
            json.dump(prefixes, pf, indent=2)

    @commands.Cog.listener()
    async def on_member_join(self, ctx, member):
        with open("configs/prefixes.json") as pf:
            p = json.load(pf)[str(ctx.message.guild.id)]
        await ctx.send(f"Hello, **{member}**! Welcome to hell, also known as **{member.guild.name}**!\n"
                       f"See `{p}info` for more information about me.")

    @commands.Cog.listener()
    async def on_member_leave(self, ctx, member):
        await ctx.send(f"Goodbye, **{member}**!")


def setup(bot):
    bot.add_cog(Events(bot))
