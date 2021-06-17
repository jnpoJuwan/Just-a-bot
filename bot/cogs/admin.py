import io
import textwrap
import traceback
from contextlib import redirect_stdout

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

    @staticmethod
    def cleanup_code(content):
        # Remove ```py\n```.
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # Remove `foo`.
        return content.strip('` \n')

    # CRED: @Rapptz (https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py#L216)
    @commands.command(name='eval', pass_context=True)
    @checks.is_admin()
    async def eval_(self, ctx, *, body: str):
        """Evaluates Python code."""
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()
        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except:
            value = stdout.getvalue()
            await ctx.send(f'```\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```\n{value}{ret}\n```')

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
