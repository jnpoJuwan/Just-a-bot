from random import choice

import discord
from discord.ext import commands

from ._utils import exceptions


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # I am trying to make the command below work with roles.
    # No success thus far (Someone help me aaaaaaaaaaaaaa).

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member = None):
        """Kiss the given member.

        If no member is specified, kiss a random member."""
        if member is None:
            member = choice(ctx.guild.members)

        await member.send(f"{ctx.author.display_name} kissed you.")
        await ctx.send(f"You kissed {member.mention}.")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def fuck(self, ctx, member: discord.Member = None):
        """Fuck the given member.

        If no member is specified, fuck a random member."""
        if member is None:
            member = choice(ctx.guild.members)

        await member.send(f"{ctx.author.display_name} fucking destroyed your fragile asshole.")
        await ctx.send(f"You destroyed {member.mention}'s fragile asshole.")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def poke(self, ctx, member: discord.Member = None):
        """Poke the given member.

        If no member is specified, poke a random member."""
        if member is None:
            member = choice(ctx.guild.members)

        await member.send(f"{ctx.author.display_name} poked you.")
        await ctx.send(f"You poked {member.mention}.")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member = None):
        """Slap the given member.

        If no member is specified, slap a random member."""
        if member is None:
            member = choice(ctx.guild.members)

        await member.send(f"{ctx.author.display_name} slapped you.")
        await ctx.send(f"You slapped {member.mention}.")

    # Exception Handling.

    @kiss.error
    @fuck.error
    @poke.error
    @slap.error
    async def action_error(self, error):
        if isinstance(error, commands.BadArgument):
            raise exceptions.MemberNotFoundError


def setup(bot):
    bot.add_cog(Actions(bot))
