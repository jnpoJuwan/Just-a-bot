import discord
from discord.ext import commands

from just_a_bot.configs.constants import COLOUR

FMT = "%A, %B %d %H:%M UTC"


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command(aliases=["emoji"])
    async def emoji_info(self, ctx, emoji):
        async with ctx.typing():
            embed = discord.Embed(title=f"{str(emoji)} {emoji.name}", colour=COLOUR)
        await ctx.send(embed=embed)

    @commands.command(aliases=["member"])
    async def member_info(self, ctx, member: discord.Member = None):
        """Send an embed with the member's information."""
        if member is None:
            member = ctx.author

        roles = [role for role in member.roles]

        async with ctx.typing():
            embed = discord.Embed(title=str(member), colour=COLOUR)
            embed.add_field(name="Nickname", value=member.display_name)
            embed.add_field(name="Top Role", value=member.top_role.mention)
            embed.add_field(name=f"Roles ({len(roles)})", value="\n".join([role.mention for role in roles]))
            embed.add_field(name="Account Created at:", value=member.created_at.strftime(FMT))
            embed.add_field(name="Joined at:", value=member.joined_at.strftime(FMT))
            embed.add_field(name="Member ID", value=member.id)
            embed.add_field(name="Member Hash", value=str(hash(member)))
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["guild", "server", "server_info"])
    async def guild_info(self, ctx):
        """Send an embed with the guild's information."""
        guild = ctx.guild

        async with ctx.typing():
            embed = discord.Embed(title=guild.name, colour=COLOUR)
            embed.set_thumbnail(url=str(guild.icon_url))
            embed.add_field(name="Server Owner", value=f"<@{guild.owner_id}>")
            embed.add_field(name="Server Region", value=str(guild.region).title())
            embed.add_field(name="Member Count", value=str(ctx.guild.member_count))
            embed.add_field(name="Created at:", value=guild.created_at.strftime(FMT))
            embed.add_field(name="Server ID", value=guild.id)
            embed.add_field(name="Server Hash", value=str(hash(guild)))
            embed.set_thumbnail(url=guild.icon_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["source"])
    async def source_code(self, ctx):
        """Send the bot's source code."""
        embed = discord.Embed(title="Source Code",
                              description="https://github.com/jnpoJuwan/just_a_bot",
                              colour=COLOUR)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    # Exception Handling.

    @member_info.error
    async def member_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please @mention a member.")


def setup(bot):
    bot.add_cog(Information(bot))
