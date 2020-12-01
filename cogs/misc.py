import random

import discord
from discord.ext import commands


SPAM_LIMIT = 25


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # IDEA: _eval(self, ctx, code): Evaluate code.
    # IDEA: is_down(self, ctx, service): Send True if the service is down, False otherwise.
    # IDEA: jankenpon(self, ctx): Play "Rock, Paper, Scissors".

    # cogs/music.py:
    # IDEA: join_voice_channel(self, ctx): Connect into the voice channel that the user is in.
    # IDEA: leave_voice_channel(self, (ctx)

    @commands.command(aliases=["coin_flip", "heads", "tails"])
    async def flip_coin(self, ctx, amount: int = 1):
        """Flips a coin of the input amount of times."""
        for i in range(amount):
            await ctx.send(f"**{random.choice(['Heads', 'Tails'])}**")

    @commands.command()
    async def choose(self, ctx, *args):
        """Send a random choice."""
        for arg in args:
            arg.replace(",", " ")
        await ctx.send(f"**{random.choice(args)}**")

    @commands.command(aliases=["map", "random_map"])
    async def choose_map(self, ctx):
        """Send a random Among Us map."""
        outcomes = "The Skeld", "MIRA HQ", "Polus"
        await ctx.send(f"You should play in **{random.choice(outcomes)}.**")

    @commands.command(aliases=["dm", "pm", "private_message"])
    async def direct_message(self, ctx):
        """Send a nice private message."""
        await ctx.author.send("**pong pong, motherpinger.**")

    @commands.command(aliases=["say"])
    async def echo(self, ctx, *, message="echo"):
        """Echo the user's input-message."""
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(aliases=["fuck", "fuckyou", "f*ck_you"])
    async def fuck_you(self, ctx):
        """Send response to 'fuck you'."""
        await ctx.send("Fuck my robot body yourself, you fucking coward :rage:.", tts=True)

    @commands.command(aliases=["unsleep", "wakeupyouuselessbot"])
    async def login(self, ctx):
        await ctx.send("Fuck off, <@569435621190270976>.")

    @commands.command(name="8ball", aliases=["8-ball", "ball8", "magic_8-ball"])
    async def magic_8ball(self, ctx, *, question="???"):
        """Send and choose a random Magic 8-Ball answer."""
        # SEE: https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
        outcomes = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
                    "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                    "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
                    "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
                    "My sources say no.", "Outlook not so good.", "Very doubtful."]
        await ctx.send(f"> {question}\n**{random.choice(outcomes)}**")

    @commands.command()
    async def ping(self, ctx):
        """Send 'pong'."""
        await ctx.send("pong")

    @commands.command(aliases=["pang", "peng", "pung", "pyng"])
    async def pong(self, ctx):
        """Send 'ping' (sike)."""
        await ctx.send("No! This isn't how you're supposed to play the game.")

    @commands.command(aliases=["cock", "dick", "peen", "peenis", "pepe", "pp"])
    async def penis(self, ctx, member=None):
        """Send a random dick penis size."""
        if member is None:
            member = ctx.author

        if member == discord.Role:
            raise commands.BadArgument

        await ctx.send(f"This is <@{member.id}>'s penis: **8{'=' * random.randint(0, 9)}D**")

    @commands.command()
    async def umlaut(self, ctx, *, text="None"):
        """Add an umlaut to every vowel in the message."""
        for vowel in "aeiouyAEIOUY":
            text = text.replace(vowel, vowel + "\u0308")
        await ctx.send(text)

    @commands.command()
    async def words(self, ctx, *, text):
        """Send the amount of words in the message's content."""
        await ctx.send(f"**{len(text.split())}**")

    # Exception Handling

    @penis.error
    async def member_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please @mention a member.")


def setup(bot):
    bot.add_cog(Misc(bot))
