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
        """Kiss a member. Kiss a random member if no member is specified."""
        if member is None:
            member = choice(ctx.guild.members)

        await member.send(f"{ctx.author.name} kissed you.")
        await ctx.send(f"You kissed {member},")

    @commands.command()
    async def fuck(self, ctx, member: discord.Member = None):
        """Fuck a member. Fuck a random member if no member is specified."""
        if member is None:
            member = choice(ctx.guild.members)

        await member.send(f"{ctx.author.name} fucking destroyed your fragile asshole.")
        await ctx.send(f"You fucking destroyed {member}'s fragile asshole.")

    @commands.command()
    async def poke(self, ctx, member: discord.Member = None):
        """Poke a member. Poke a random member if no member is specified."""
        if member is None:
            member = choice(ctx.guild.members)

        await member.send(f"{ctx.author.name} poked you.")
        await ctx.send(f"You poked {member},")

    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        """Slap a member. Slap a random member if no member is specified."""
        if member is None:
            member = choice(ctx.guild.members)

        await member.send(f"{ctx.author.name} slapped you.")
        await ctx.send(f"You slapped {member},")

    @kiss.error
    @fuck.error
    @poke.error
    @slap.error
    async def action_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please @mention a member.")


def setup(bot):
    bot.add_cog(Actions(bot))
