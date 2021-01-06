import json

import discord
from discord.ext import commands

from ._utils import checks, exceptions
from ._utils.constants import COLOUR, DEFAULT_PREFIX

FMT = "%A, %B %d %H:%M UTC"


class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    @commands.command()
    async def member_info(self, ctx, member: discord.Member = None):
        """Send an embed with the given member's information."""
        member = member or ctx.author
        roles = [role.mention for role in member.roles]

        async with ctx.typing():
            embed = discord.Embed(title=str(member), colour=COLOUR)
            embed.add_field(name="Nickname", value=member.display_name)
            embed.add_field(name="Top Role", value=member.top_role.mention)
            embed.add_field(name=f"Roles ({len(roles)})", value="\n".join(roles))
            embed.add_field(name="Created", value=member.created_at.strftime(FMT))
            embed.add_field(name="Joined", value=member.joined_at.strftime(FMT))
            embed.add_field(name="User ID", value=member.id)
            # embed.add_field(name="User Hash", value=str(hash(member)))
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["server_info"])
    async def guild_info(self, ctx):
        """Send an embed with the guild's information."""
        guild = ctx.guild

        async with ctx.typing():
            embed = discord.Embed(title=guild.name, colour=COLOUR)
            embed.set_thumbnail(url=str(guild.icon_url))
            embed.add_field(name="Server Owner", value=f"<@{guild.owner_id}>")
            embed.add_field(name="Server Region", value=str(guild.region).title())
            embed.add_field(name="Member Count", value=str(ctx.guild.member_count))
            embed.add_field(name="Created", value=guild.created_at.strftime(FMT))
            embed.add_field(name="Server ID", value=guild.id)
            embed.add_field(name="Server Hash", value=str(hash(guild)))
            embed.set_thumbnail(url=guild.icon_url)
            embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def icon(self, ctx):
        """Send the guild's icon."""
        async with ctx.typing():
            embed = discord.Embed(title=f"Icon of {ctx.guild.name}", colour=COLOUR)
            embed.set_image(url=ctx.guild.icon_url)
            embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["avatar", "profile_picture"])
    async def pfp(self, ctx, member: discord.Member = None):
        """Send the profile picture of the given member."""
        member = member or ctx.author

        async with ctx.typing():
            embed = discord.Embed(title=f"{member.display_name}'s profile picture", colour=COLOUR)
            embed.set_image(url=member.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["source"])
    async def source_code(self, ctx):
        """Send an embed with the bot's source code."""
        embed = discord.Embed(title="Source Code", description="https://github.com/jnpoJuwan/just_a_bot",
                              colour=COLOUR)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.group()
    async def settings(self, ctx):
        pass

    @settings.command(aliases=["prefix"])
    @commands.guild_only()
    @checks.is_admin()
    async def change_prefix(self, ctx, prefix=None):
        """Change the guild's prefix."""
        prefix = prefix or DEFAULT_PREFIX
        path = "configs/prefixes.json"

        with open(path) as f:
            prefixes = json.load(f)
            prefixes[str(ctx.guild.id)] = prefix
        with open(path, "w") as f:
            json.dump(prefixes, f, indent=2, sort_keys=True)
        await ctx.send(f"The server's prefix has been changed to `{prefix}`.")

    # Exception Handling.

    @member_info.error
    async def member_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please @mention a member.")


def setup(bot):
    bot.add_cog(Meta(bot))
