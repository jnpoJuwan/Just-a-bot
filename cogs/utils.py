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
        print(f"INFO: {__name__} is ready.")

    # IDEA: is_down(self, ctx, service): Send True if the service is down, False otherwise.

    # This command can be used for malicious purposes.
    # CREDIT: @nitros12 (GitHub)
    @commands.command(name="eval")
    # @checks.is_bot_owner()
    async def eval_(self, ctx, *, cmd):
        """Evaluate the input.
        Input is interpreted as newline separated statements.
        If the last statement is an expression, that is the return value.

        Such that `!eval 1 + 1` gives `2` as the result.
        The following invocation will cause the bot to send the text '9'
        to the channel of invocation and return '3' as the result of evaluating

        !eval ```
        a = 1 + 2
        b = a * 2
        await ctx.send(a + b)
        a
        ```
        """

        env = {
            "__import__": __import__,
            "author": ctx.author,
            "bot": ctx.bot,
            "ctx": ctx,
            "commands": commands,
            "discord": discord,
            "guild": ctx.guild,
            "message": ctx.message,
        }

        fn_name = "_eval_expr"
        cmd = cmd.strip("` ")

        # Add a layer of indentation.
        cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

        # Wrap in async def body.
        body = f"async def {fn_name}():\n{cmd}"
        parsed = ast.parse(body)
        body = parsed.body[0].body

        insert_returns(body)

        exec(compile(parsed, filename="<ast>", mode="exec"), env)
        result = (await eval(f"{fn_name}()", env))
        await ctx.send(result)

    @commands.command(aliases=["coin_flip", "heads", "tails"])
    async def flip_coin(self, ctx, amount=1):
        """Flips a coin of the input amount of times."""
        if amount <= SPAM_LIMIT:
            for i in range(amount):
                await ctx.send(f"**{random.choice(['Heads', 'Tails'])}**")
        else:
            raise exceptions.SpamError

    @commands.command()
    async def get_prefix(self, ctx):
        """Send the server's prefix."""
        with open("configs/prefixes.json") as pf:
            p = json.load(pf)[str(ctx.message.guild.id)]
        await ctx.send(f"The server's prefix is `{p}`.")

    @commands.command(aliases=["len"])
    async def length(self, ctx, *, text):
        """Send the length of the message's content"""
        await ctx.send(f"**{len(text)}**")

    @commands.command()
    async def random(self, ctx):
        """Send a random number in the range [0, 1) or [0, 1] depending on rounding."""
        await ctx.send(f"**{random.random()}**")

    @commands.command(aliases=["dice", "randint"])
    async def roll(self, ctx, *, b=20, amount=1):
        """Send a random integer in range [1, b], including both end points, an amount of times."""
        if b < 1:
            raise commands.BadArgument
        else:
            if amount <= SPAM_LIMIT:
                for i in range(amount):
                    await ctx.send(f"**{random.randint(1, b)}**")
            else:
                raise exceptions.SpamError

    @commands.command()
    async def words(self, ctx, *, text):
        """Send the amount of words in the message's content."""
        await ctx.send(f"**{len(text.split())}**")

    # Exception Handling.

    @eval_.error
    async def eval_error(self, ctx, error):
        if not isinstance(error, commands.UserInputError):
            await ctx.send(error)

    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please input a positive integer (Use `!random` for rationals).")


def setup(bot):
    bot.add_cog(Utils(bot))
