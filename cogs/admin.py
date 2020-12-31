import json

import discord
from discord.ext import commands

from ._utils import checks
from ._utils.constants import DEFAULT_PREFIX
from ._utils.logger import logger


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban the given member."""
        if ctx.author == member:
            await ctx.send("You can't ban yourself.")

        if not reason:
            await member.ban()
            await ctx.send(f"{member.mention} was banned by {ctx.author.mention}.")
        else:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} was banned by {ctx.author.mention}.\n[Reason: {reason}]")

    @commands.command(aliases=["prefix"])
    @commands.guild_only()
    @checks.is_admin()
    async def change_prefix(self, ctx, prefix=None):
        """Change the guild's prefix.

        If no prefix is specified, change the prefix to the bot's default prefix.
        """
        if not prefix:
            prefix = DEFAULT_PREFIX
        if len(prefix) > 6:
            await ctx.send("The prefix can't exceed 6 characters in length.\nShortening prefix...")
            prefix = prefix[:6]

        with open("configs/prefixes.json") as pf:
            prefixes = json.load(pf)
        with open("configs/prefixes.json", "w") as pf:
            prefixes[str(ctx.guild.id)] = prefix
            json.dump(prefixes, pf, indent=2)
        await ctx.send(f"The server's prefix has changed to `{prefix}`.")

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick the given member."""
        if ctx.author == member:
            await ctx.send("You can't kick yourself.")

        if not reason:
            await member.kick()
            await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}.")
        else:
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}.\n[Reason: {reason}]")

    @commands.command(aliases=["die", "disconnect", "quit", "sleep"])
    @checks.is_admin()
    async def logout(self, ctx):
        """Logout from Discord."""
        await ctx.send("**change da world**\n**my final message. Goodb ye**")
        logger.critical("Bot has logged out.")
        await self.bot.logout()

    @commands.command(aliases=["clear", "delete"])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    @checks.is_mod()
    async def purge(self, ctx, limit=0):
        """Purge the given amount of messages."""
        if limit > 200:
            await ctx.send("The amount can't exceed 200 messages.")
        await ctx.message.delete()
        await ctx.channel.purge(limit=limit)
        await ctx.send(f"Purged {limit} message(s).", delete_after=2.5)

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def unban(self, ctx, user_id):
        """Unban the given user."""
        user = self.bot.get_user(user_id=user_id)
        await ctx.guild.unban(user)
        await ctx.send(f"{user} was unbanned by {ctx.author.mention}.")

    # Exception Handling.

    @ban.error
    @kick.error
    async def kickban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please @mention a member.")

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please insert a positive integer.")


def setup(bot):
    bot.add_cog(Admin(bot))
