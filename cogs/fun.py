import random

import discord
from discord.ext import commands

from ..configs.constants import COLOUR


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")

    # IDEA: jankenpon(self, ctx): Play "Rock, Paper, Scissors".

    @commands.command(name="8ball", aliases=["8-ball", "magic_8ball", "magic_8-ball"])
    async def _8ball(self, ctx, *, question="???"):
        """Send and choose a random Magic 8-Ball answer."""
        # SEE: https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
        outcomes = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
                    "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                    "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
                    "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
                    "My sources say no.", "Outlook not so good.", "Very doubtful."]
        await ctx.send(f"> {question}\n**{random.choice(outcomes)}**")

    @commands.command(aliases=["cock_and_ball_torture"])
    async def cbt(self, ctx):
        """Send an embed with the summary for the Wikipedia page of "Cock and ball torture"."""
        # SEE: https://en.wikipedia.org/wiki/Cock_and_ball_torture
        async with ctx.typing():
            summary = "**Cock and ball torture** (**CBT**), penis torture or dick torture is a sexual activity " \
                      "involving application of pain or constriction to the penis or testicles." \
                      "This may involve directly painful activities, such as genital piercing, wax play, genital " \
                      "spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic " \
                      "electrostimulation, kneeing or kicking. The recipient of such activities may receive direct " \
                      "physical pleasure via masochism, or emotional pleasure through erotic humiliation, " \
                      "or knowledge that the play is pleasing to a sadistic dominant. " \
                      "Many of these practices carry significant health risks."

            embed = discord.Embed(title="Cock and ball torture", description=summary, colour=COLOUR)
            embed.add_field(name="External Link", value="https://en.wikipedia.org/wiki/Cock_and_ball_torture")
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def choose(self, ctx, *args):
        """Send a random choice."""
        for arg in args:
            arg.strip(",")
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
    async def echo(self, ctx, *, text="echo"):
        """Echo the user's input-message."""
        await ctx.send(text)

    @commands.command(aliases=["fuckyou", "f*ck_you"])
    async def fuck_you(self, ctx):
        """Send response to 'fuck you'."""
        await ctx.send("Fuck my robot body yourself, you fucking coward :rage:.")

    @commands.command(aliases=["cock", "dick", "pepe", "pp"])
    async def penis(self, ctx, member=None):
        """Send a random penis size."""
        if not member:
            member = ctx.author

        await ctx.send(f"This is <@{member.id}>'s penis: **8{'=' * random.randint(0, 9)}D**")

    @commands.command()
    async def ping(self, ctx):
        """Send "pong"."""
        await ctx.send("pong")

    @commands.command()
    async def poll(self, ctx, *, question):
        """Create a basic poll."""
        embed = discord.Embed(title="Poll", description=question, colour=COLOUR)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        message = await ctx.send(embed=embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷')

    @commands.command(aliases=["pang", "peng", "pung", "pyng"])
    async def pong(self, ctx):
        """Send "ping" (sike)."""
        await ctx.send("No! This isn't how you're supposed to play the game.")

    @commands.command()
    async def umlaut(self, ctx, *, text="None"):
        """Add an umlaut to every vowel in the message."""
        for vowel in "aeiouyAEIOUY":
            text = text.replace(vowel, vowel + "\u0308")

        await ctx.send(text)

    # Exception Handling.

    @penis.error
    async def member_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please @mention a member.")


def setup(bot):
    bot.add_cog(Fun(bot))
