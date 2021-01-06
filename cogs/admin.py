import discord
from discord.ext import commands

from ._utils import checks


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # Administration commands.

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban the given member."""
        if member == ctx.author:
            await ctx.send("You can't ban yourself.")

        if reason:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} was banned by {ctx.author.mention}.\n[Reason: {reason}]")
        else:
            await member.ban()
            await ctx.send(f"{member.mention} was banned by {ctx.author.mention}.")

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick the given member."""
        if member == ctx.author:
            await ctx.send("You can't kick yourself.")

        if reason:
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}.\n[Reason: {reason}]")
        else:
            await member.kick()
            await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}.")

    @commands.command(aliases=["die", "disconnect", "quit", "sleep"])
    @checks.is_admin()
    async def logout(self, ctx):
        """Logout from Discord."""
        await ctx.send("**change da world**\n**my final message. Goodb ye**")
        await self.bot.logout()

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def unban(self, ctx, user_id):
        """Unban the given user."""
        user = self.bot.get_user(user_id=user_id)
        await ctx.guild.unban(user)
        await ctx.send(f"{user} was unbanned by {ctx.author.mention}.")

    # Moderation commands.

    @commands.command(aliases=["clear", "delete"])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    @checks.is_mod()
    async def purge(self, ctx, limit=0):
        """Purge the given amount of messages."""
        if limit > 100:
            await ctx.send("The amount can't exceed 100 messages.")
        await ctx.message.delete()
        await ctx.channel.purge(limit=limit)
        await ctx.send(f"Purged {limit} message(s).", delete_after=2.5)

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
