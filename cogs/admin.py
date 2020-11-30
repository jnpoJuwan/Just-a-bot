import json
import os

import discord
from discord.ext import commands

from just_a_bot.utils import checks


COGS = [file for file in os.listdir("cogs") if file.endswith(".py") and not file.startswith("_")]


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # IDEA: mute(self, ctx, member)
    # IDEA: unmute(self, ctx, member)

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban the member."""
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned by {ctx.author.mention}.\n[Reason: {reason}]")

    @commands.command()
    async def get_prefix(self, ctx):
        """Send the server's prefix."""
        with open("configs/prefixes.json") as pf:
            p = json.load(pf)[str(ctx.message.guild.id)]
        await ctx.send(f"The server's prefix is `{p}`.")

    @commands.command(aliases=["prefix"])
    @commands.guild_only()
    @checks.is_admin()
    async def change_prefix(self, ctx, prefix=None):
        """Change the guild's prefix."""
        if not prefix:
            prefix = self.bot.default_prefix

        if len(prefix) > 5:
            await ctx.send("The prefix can't exceed 5 characters in length.")
        else:
            with open("configs/prefixes.json") as pf:
                prefixes = json.load(pf)
            with open("configs/prefixes.json", "w") as pf:
                prefixes[str(ctx.guild.id)] = prefix
                json.dump(prefixes, pf, indent=2)
            await ctx.send(f"The server's prefix has changed to `{prefix}`.")

    @commands.command(aliases=["change_nickname"])
    @commands.guild_only()
    @checks.is_admin()
    async def change_nick(self, ctx, member: discord.Member, nick):
        """Change the member's nickname."""
        await member.edit(nick=nick)
        await ctx.send(f"Their nickname has changed to {nick}.")

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick the member."""
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}.\n[Reason: {reason}]")

    @commands.command(aliases=["die", "disconnect", "quit", "sleep"])
    @checks.is_admin()
    async def logout(self, ctx):
        """Logout from the server."""
        await ctx.send("**change da world**\n**my final message. Goodb ye**")
        await self.bot.logout()

    @commands.command(aliases=["clear", "delete"])
    @checks.is_mod()
    async def purge(self, ctx, limit: int = 0):
        """Purge the amount limit of messages."""
        await ctx.message.delete()
        await ctx.channel.purge(limit=limit)
        await ctx.send(f"Purged {limit} message(s).", delete_after=2.5)

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def unban(self, ctx, user_id: int):
        """Unban the user."""
        user = self.bot.get_user(user_id=user_id)
        await ctx.guild.unban(user)
        await ctx.send(f"{user} was unbanned by {ctx.author.mention}")

    # Bot Developer Misc.

    @commands.command()
    @checks.is_developer()
    async def load(self, ctx, cog=None):
        """Load a cog."""
        if not cog:
            for file in COGS:
                async with ctx.typing():
                    self.bot.load_extension(f"cogs.{file.lower()[:-3]}")
                await ctx.send(f"**`cogs.{file.lower()[:-3]}` has been loaded.**")
        else:
            file = f"{cog.lower()}.py"
            if not os.path.exists(f"cogs/{file}"):
                raise commands.BadArgument
            elif file.endswith(".py") and not file.startswith("_"):
                async with ctx.typing():
                    self.bot.load_extension(f"cogs.{file[:-3]}")
                await ctx.send(f"**`cogs.{file[:-3]}` has been loaded.**")

    @commands.command()
    @checks.is_developer()
    async def unload(self, ctx, cog=None):
        """Unload a cog."""
        if not cog:
            for file in COGS:
                async with ctx.typing():
                    self.bot.unload_extension(f"cogs.{file.lower()[:-3]}")
                await ctx.send(f"**`cogs.{file.lower()[:-3]}` has been unloaded.**")
        else:
            file = f"{cog.lower()}.py"
            if not os.path.exists(f"cogs/{file}"):
                raise commands.BadArgument
            elif file.endswith(".py") and not file.startswith("_"):
                async with ctx.typing():
                    self.bot.unload_extension(f"cogs.{file[:-3]}")
                await ctx.send(f"**`cogs.{file[:-3]}` has been unloaded.**")

    @commands.command()
    @checks.is_developer()
    async def reload(self, ctx, cog=None):
        """Reload either a cog or all cogs."""
        if not cog:
            for file in COGS:
                async with ctx.typing():
                    self.bot.reload_extension(f"cogs.{file.lower()[:-3]}")
                await ctx.send(f"**`cogs.{file.lower()[:-3]}` has been reloaded.**")
        else:
            file = f"{cog.lower()}.py"
            if not os.path.exists(f"cogs/{file}"):
                raise commands.BadArgument
            elif file.endswith(".py") and not file.startswith("_"):
                async with ctx.typing():
                    self.bot.reload_extension(f"cogs.{file[:-3]}")
                await ctx.send(f"**`cogs.{file[:-3]}` has been reloaded.**")

    # Exception Handling

    @ban.error
    @kick.error
    async def kickban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please input must be a member mention.")

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please insert a positive integer.")

    @load.error
    @unload.error
    @reload.error
    async def load_cogs_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Sorry. I can't find that cog.")


def setup(bot):
    bot.add_cog(Admin(bot))
