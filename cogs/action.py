from random import choice

import discord
from discord.ext import commands


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        """Kiss a member."""
        if member is None:
            member = choice(ctx.guild.members)
        await member.send(f"{ctx.author.name} kissed you.")

    @commands.command()
    async def poke(self, ctx, member: discord.Member = None):
        """Poke a member."""
        if member is None:
            member = choice(ctx.guild.members)
        await member.send(f"{ctx.author.name} poked you.")

    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        """Slap a member."""
        if member is None:
            member = choice(ctx.guild.members)
        await member.send(f"{ctx.author.name} slapped you.")

    @kiss.error
    @poke.error
    @slap.error
    async def action_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please @mention a member.")


def setup(bot):
    bot.add_cog(Actions(bot))
