import ast
import json
import random

import discord
from discord.ext import commands

from ._utils.constants import SPAM_LIMIT
from ._utils import exceptions


def insert_returns(body):
    # Insert return statement if the last expression is a expression statement.
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # For if statements, we insert returns into the body and the or else.
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # For with blocks, again we insert returns into the body.
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'INFO: {__name__} is ready.')

    # IDEA: is_down(self, ctx, service): Send True if the service is down, False otherwise.

    @commands.command()
    async def choose(self, ctx, *args):
        """Choose a random element from the given arguments."""
        map(lambda x: x.strip(','), args)
        await ctx.send(f'**{random.choice(args)}**')

    # This command can be used for malicious purposes.
    # CREDIT: @nitros12 (GitHub [https://gist.github.com/nitros12/2c3c265813121492655bc95aa54da6b9])
    @commands.command(name='eval')
    # checks.is_admin()
    async def eval_(self, ctx, *, cmd):
        """Evaluate the given source.

        Input is interpreted as newline separated statements.
        If the last statement is an expression, that is the return value.

        Such that `!eval 1 + 1` gives `2` as the result.
        """
        env = {
            '__import__': __import__,
            'author': ctx.author,
            'bot': ctx.bot,
            'ctx': ctx,
            'commands': commands,
            'discord': discord,
            'guild': ctx.guild,
            'message': ctx.message,
        }

        fn_name = '_eval_expr'
        cmd = cmd.strip('` ')

        # Add a layer of indentation.
        cmd = '\n'.join(f'    {i}' for i in cmd.splitlines())

        # Wrap in async def body.
        body = f'async def {fn_name}():\n{cmd}'
        parsed = ast.parse(body)
        body = parsed.body[0].body

        insert_returns(body)

        exec(compile(parsed, filename='<ast>', mode='exec'), env)
        result = (await eval(f'{fn_name}()', env))
        await ctx.send(result)

    @commands.command(aliases=['coin_flip', 'heads', 'tails'])
    async def flip_coin(self, ctx, amount=1):
        """Flip a coin of the given amount of times."""
        if amount >= SPAM_LIMIT:
            raise exceptions.SpamError
        else:
            for _ in range(amount):
                await ctx.send(f'**{random.choice(["Heads", "Tails"])}**')

    @commands.command(aliases=['prefix'])
    async def get_prefix(self, ctx):
        """Get the guild's prefix."""
        with open('configs/prefixes.json') as f:
            p = json.load(f)[str(ctx.message.guild.id)]
        await ctx.send(f'This server\'s prefix is `{p}`.')

    @commands.command(aliases=['len'])
    async def length(self, ctx, *, text):
        """Send the length of the given text."""
        await ctx.send(f'**{len(text)}**')

    @commands.command()
    async def random(self, ctx):
        """Send a random number in the range [0, 1) or [0, 1] depending on rounding."""
        await ctx.send(f'**{random.random()}**')

    @commands.command(aliases=['dice', 'randint'])
    async def roll(self, ctx, *, b=20, amount=1):
        """Send a random integer in range [1, b], including both end points, an amount of times."""
        if b < 1:
            await ctx.send('Please input a positive integer (Use `!random` for rationals).')
        else:
            if amount >= SPAM_LIMIT:
                raise exceptions.SpamError
            else:
                for _ in range(amount):
                    await ctx.send(f'**{random.randint(1, b)}**')

    @commands.command()
    async def sort(self, ctx, *iterable):
        """Send a new list containing all items from the given iterable in ascending order."""
        map(lambda x: x.strip(','), iterable)
        await ctx.send(' '.join(sorted(iterable)))

    @commands.command()
    async def words(self, ctx, *, text):
        """Send the amount of words in the message's content."""
        await ctx.send(f'**{len(text.split())}**')

    # Exception Handling.

    @eval_.error
    async def eval_error(self, ctx, error):
        if not isinstance(error, commands.UserInputError):
            await ctx.send(error)


def setup(bot):
    bot.add_cog(Utils(bot))
