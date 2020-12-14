import discord
from discord.ext import commands

from .embeds import COLOUR


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command()
    async def cat(self, ctx):
        """Send a cat picture."""
        # async with aiohttp.ClientSession() as cs:
        #     async with cs.get("http://aws.random.cat//meow") as r:
        #         res = await r.json()
        #         image = res["file"]
        # async with aiohttp.ClientSession() as cs:
        #     async with cs.get("https://some-random-api.ml/facts/cat") as r:
        #         res = await r.json()
        #         fact = res["fact"]
        #
        # embed = discord.Embed(title="Kitty!", color=COLOUR)
        # embed.add_field(name="Random Cat Fact", value="{fact}")
        # await ctx.send(embed=embed)

    @commands.command()
    async def icon(self, ctx):
        """Send the server's icon."""
        async with ctx.typing():
            embed = discord.Embed(title=f"{ctx.guild.name}'s icon", colour=COLOUR)
            embed.set_image(url=ctx.guild.icon_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=["avatar", "profile_picture"])
    async def pfp(self, ctx, member: discord.Member = None):
        """Send the profile picture of a member. Send the author's profile picture if no member is specified."""
        if member is None:
            member = ctx.author

        async with ctx.typing():
            embed = discord.Embed(title=f"{member}'s avatar", colour=COLOUR)
            embed.set_image(url=member.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    # Exception Handling.

    @pfp.error
    async def member_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please @mention a member.")


def setup(bot):
    bot.add_cog(Images(bot))
