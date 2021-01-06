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

    # FIXME: Make commands work with roles.

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def cuddle(self, ctx, member: discord.Member = None):
        """Cuddle the given member."""
        member = member or choice(ctx.guild.members)
        await member.send(f"{ctx.author.display_name} cuddled you.")
        await ctx.send(f"You cuddled {member.mention}.")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def cry(self, ctx, member: discord.Member = None):
        """Cry on the given member's shoulder."""
        member = member or choice(ctx.guild.members)
        await member.send(f"{ctx.author.display_name} cried on your shoulder.")
        await ctx.send(f"You cried on {member.mention}'s shoulder.")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def fuck(self, ctx, member: discord.Member = None):
        """Fuck the given member."""
        member = member or choice(ctx.guild.members)
        await member.send(f"{ctx.author.display_name} fucking destroyed your fragile asshole.")
        await ctx.send(f"You destroyed {member.mention}'s fragile asshole.")

    @commands.command(aliases=["hand_hold", "hold_hands"])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def hold_hand(self, ctx, member: discord.Member = None):
        """Hold hands with the given member."""
        member = member or choice(ctx.guild.members)
        await member.send(f"{ctx.author.display_name} is holding your hand.")
        await ctx.send(f"You committed pre-marital hold handing with {member.mention}.")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member = None):
        """Hug the given member."""
        member = member or choice(ctx.guild.members)
        await member.send(f"{ctx.author.display_name} hugged you.")
        await ctx.send(f"You hugged {member.mention}.")

    @commands.command(aliases=["assassinate", "murder", "slaughter"])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def kill(self, ctx, member: discord.Member = None):
        """Kill the given member."""
        member = member or choice(ctx.guild.members)
        await member.send(f"{ctx.author.display_name} killed you.")
        await ctx.send(f"You have murdered {member.mention}. You are now on the FBI's wanted list")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member = None):
        """Kiss the given member."""
        member = member or choice(ctx.guild.members)
        await member.send(f"{ctx.author.display_name} kissed you.")
        await ctx.send(f"You kissed {member.mention}.")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def poke(self, ctx, member: discord.Member = None):
        """Poke the given member."""
        member = member or choice(ctx.guild.members)
        await member.send(f"{ctx.author.display_name} poked you.")
        await ctx.send(f"You poked {member.mention}.")

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member = None):
        """Slap the given member."""
        member = member or choice(ctx.guild.members)
        await member.send(f"{ctx.author.display_name} slapped you.")
        await ctx.send(f"You slapped {member.mention}.")

    # Exception Handling.

    @kiss.error
    @fuck.error
    @poke.error
    @slap.error
    async def action_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            raise exceptions.MemberNotFoundError


def setup(bot):
    bot.add_cog(Actions(bot))
