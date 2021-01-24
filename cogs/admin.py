import discord
from discord.ext import commands

from ._utils import checks


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'INFO: {__name__} is ready.')

    # Administration commands.

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban the member for a reason."""
        if member == ctx.author:
            await ctx.send('You can\'t ban yourself.')

        if reason:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} was banned by {ctx.author.mention}.\n[Reason: {reason}]')
        else:
            await member.ban()
            await ctx.send(f'{member.mention} was banned by {ctx.author.mention}.')

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick the member for a reason."""
        if member == ctx.author:
            await ctx.send('You can\'t kick yourself.')

        if reason:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} was kicked by {ctx.author.mention}.\n[Reason: {reason}]')
        else:
            await member.kick()
            await ctx.send(f'{member.mention} was kicked by {ctx.author.mention}.')

    @ban.error
    @kick.error
    async def kickban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please @mention a member.')

    @commands.command()
    @commands.guild_only()
    @checks.is_admin()
    async def unban(self, ctx, user_id: int = None):
        """Unban the user by user ID."""
        if user_id is None:
            raise commands.BadArgument

        user = self.bot.get_user(user_id=user_id)
        await ctx.guild.unban(user)
        await ctx.send(f'{user} was unbanned by {ctx.author.mention}.')

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(
                'Please insert a valid user ID.\n**Support:** '
                'https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-'
            )

    # Moderation commands.

    @commands.command(aliases=['clear', 'delete'])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    @checks.is_mod()
    async def purge(self, ctx, amount=0):
        """Purge the given amount of messages."""
        limit = 200
        if amount > limit:
            await ctx.send(f'The amount can\'t exceed {limit} messages.')
            return

        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Purged {amount} message(s).', delete_after=2.5)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please enter a positive integer.')


def setup(bot):
    bot.add_cog(Admin(bot))
