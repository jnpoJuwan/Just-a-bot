import json
import random

import discord
import wikipedia
from discord.ext import commands

from ..utils.constants import COLOUR

# SEE: https://www.reddit.com/r/copypasta/comments/jai7dh/penis_synonyms/
penis_aliases = json.load(open('bot/assets/text/penis_aliases.json'))


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball', aliases=['8-ball'])
    async def _8ball(self, ctx, *, question=None):
        """Asks the question to the Magic 8-Ball."""
        # SEE: https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers
        outcomes = (
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.'
        )

        if not question:
            await ctx.send(f'**{random.choice(outcomes)}**')
        else:
            await ctx.send(f'> {question}\n**{random.choice(outcomes)}**')

    @commands.command()
    async def cbt(self, ctx):
        """Send the Wikipedia article for 'Cock and ball torture'."""
        # SEE: https://en.wikipedia.org/wiki/Cock_and_ball_torture
        await ctx.trigger_typing()
        embed = discord.Embed(
            title='Cock and ball torture',
            url='https://en.wikipedia.org/wiki/Cock_and_ball_torture',
            description=wikipedia.summary('Cock_and_ball_torture'), colour=COLOUR
        )
        embed.set_footer(text=f'Requested by {ctx.author.display_name} | From Wikipedia, the free encyclopedia',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['say'])
    async def echo(self, ctx, *, message='echo'):
        """Echoes the user's message while also deleting it."""
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(aliases=['fuckyou', 'f*ck_you'], hidden=True)
    async def fuck_you(self, ctx):
        """Responds to 'fuck you'."""
        await ctx.send('Fuck my robot body yourself, you fucking coward :rage:.')

    @commands.command(aliases=['hey', 'hi'])
    async def hello(self, ctx):
        """Greets the member."""
        greetings = [
            'G\'day!',
            'Good afternoon!',
            'Good evening!',
            'Good morning!',
            'Hello!',
            'Hey!',
            'Hey, you!',
            'Hey, you. You\'re finally awake.',
            '*Hey~* ;)',
            'Hi!',
            'How are you?',
            'Howdy!',
            'What\'s up?'
        ]

        await ctx.send(random.choice(greetings))

    @commands.command(aliases=penis_aliases)
    async def penis(self, ctx, member: discord.Member = None):
        """Sends the member's penis size."""
        member = member or ctx.author

        if member.id == 320325816712167426 or member.id == 567488628003962880:  # PD6#1510, Dr. IPA#3047
            n = 0
        else:
            n = random.randint(0, 30)

        _penis = f'**c{"=" * n}3**'

        if member == self.bot.user:
            await ctx.send(f'{member.display_name}\'s micropenis is 32 µm long: **8D**')
        elif n < 5:
            await ctx.send(f'{member.display_name}\'s micropenis is {n} cm long: {_penis}')
        elif n < 20:
            await ctx.send(f'{member.display_name}\'s penis is {n} cm long: {_penis}')
        else:
            await ctx.send(f'{member.display_name}\'s hard monster cock is {n} cm long: {_penis}')

    @penis.error
    async def member_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please @mention a member.')

    @commands.command()
    async def ping(self, ctx):
        """Pings back."""
        await ctx.send('pong')

    @commands.command(aliases=['pang', 'peng', 'pung', 'pyng', 'pwng'], hidden=True)
    async def pong(self, ctx):
        """Pongs back."""
        await ctx.send('No! This isn\'t how you\'re supposed to play the game.')

    @commands.command(hidden=True)
    async def spam(self, ctx):
        """Spams."""
        await ctx.send(f'I\'ve already said `{ctx.prefix}spam` is *not* an available command anymore.')

    @commands.command(aliases=['diaeresis'])
    async def umlaut(self, ctx, *, text='echo'):
        """Sends the text with umlauted vowels."""
        vowels = ['a', 'e', 'i', 'j', 'o', 'u', 'w', 'y', 'A', 'E', 'I', 'J', 'O', 'U', 'W', 'Y']
        for vowel in vowels:
            text = text.replace(vowel, vowel + '\u0308')
        await ctx.send(text)


def setup(bot):
    bot.add_cog(Fun(bot))
