import discord
from discord.ext import commands

from ..utils import checks


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def ban(self, ctx, member: discord.Member, *, reason='No specific reason.'):
        """Bans the member."""
        try:
            await member.ban(reason=reason)
        except discord.HTTPException:
            await ctx.send(f'Unable to ban {member.display_name}.')
        else:
            await ctx.send(f'{member.name} was successfully banned.')

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def kick(self, ctx, member: discord.Member, *, reason='No specific reason.'):
        """Kicks the member."""
        try:
            await member.kick(reason=reason)
        except discord.HTTPException:
            await ctx.send(f'Unable to kick {member.display_name}.')
        else:
            await ctx.send(f'{member.name} was successfully kicked.')

    @ban.error
    @kick.error
    async def kickban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please @mention a member.')

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def unban(self, ctx, *, member=None):
        """Unbans the user."""
        if member is None:
            raise commands.BadArgument

        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user} was unbanned.')

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please enter the username of a member.')


def setup(bot):
    bot.add_cog(Admin(bot))
