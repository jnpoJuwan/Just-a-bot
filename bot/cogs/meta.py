import discord
from discord.ext import commands

from ..utils.constants import COLOUR


def fmt(dt=None):
    if not dt:
        return 'N/A'
    return f'{dt:%A, %d/%m/%Y %H:%M UTC}'


class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['github', 'invite', 'source_code'])
    async def links(self, ctx):
        """Sends the bot's invite link."""
        msg = (
            '[Bot Invite](https://discord.com/api/oauth2/authorize?client_id=764106437701140490&permissions=8'
            '&scope=bot)\n'
            '[Source code](https://github.com/jnpoJuwan/Just-a-bot)'
        )

        embed = discord.Embed(title='Links', description=msg, colour=COLOUR)
        await ctx.send(embed=embed)

    @commands.command(aliases=['member', 'user', 'user_info'])
    async def member_info(self, ctx, member: discord.Member = None):
        """Sends some information about the member."""
        member = member or ctx.author
        roles = [role.mention for role in member.roles if role.name != '@everyone'][::-1]
        top_role = (member.top_role.mention if member.top_role.name != '@everyone' else member.top_role.name)

        embed = discord.Embed(colour=COLOUR)
        embed.set_author(name=str(member), icon_url=member.avatar_url)
        embed.add_field(name='Nickname', value=member.display_name)
        embed.add_field(name='Top Role', value=top_role)
        embed.add_field(name=f'Roles ({len(roles)})',
                        value=' '.join(roles) if len(roles) <= 10 else ' '.join(roles[:10]) + ' ...')
        embed.add_field(name='Created:', value=fmt(member.created_at))
        embed.add_field(name='Joined:', value=fmt(member.joined_at))
        embed.add_field(name='User ID', value=member.id)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @member_info.error
    async def member_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please @mention a member.')

    @commands.command(aliases=['server'])
    async def server_info(self, ctx):
        """Sends some information about the server."""
        guild = ctx.guild

        embed = discord.Embed(title=guild.name, colour=COLOUR)
        embed.set_thumbnail(url=str(guild.icon_url))
        embed.add_field(name='Owner', value=f'<@{guild.owner_id}>')
        embed.add_field(name='Region', value=str(guild.region).title())
        embed.add_field(name='Member Count', value=str(ctx.guild.member_count))
        embed.add_field(name='Created:', value=fmt(guild.created_at))
        embed.add_field(name='Server ID', value=guild.id)
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def icon(self, ctx):
        """Sends the server's icon."""
        embed = discord.Embed(title=f'Icon of {ctx.guild.name}', colour=COLOUR)
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['pfp'])
    async def avatar(self, ctx, member: discord.Member = None):
        """Sends the member's avatar."""
        member = member or ctx.author

        embed = discord.Embed(title=f'{member.display_name}\'s profile picture', colour=COLOUR)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meta(bot))
