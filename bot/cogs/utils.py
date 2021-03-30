import io
import json
import textwrap
import traceback
import random
from contextlib import redirect_stdout

import discord
from async_cse import Search
from discord.ext import commands
from googletrans import Translator
from wiktionaryparser import WiktionaryParser

from ..configs.configs import GOOGLE_API_KEY
from ..utils import exceptions
from ..utils.constants import COLOUR, SPAM_LIMIT
from ..utils.paginator import ListPaginator

LANGUAGE_CODES = json.load(open('bot/assets/text/language_codes.json'))


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.google_client = Search(GOOGLE_API_KEY)
        self.parser = WiktionaryParser()
        self.translator = Translator()

    @commands.command()
    async def choose(self, ctx, *args):
        """Chooses a random item from the list."""
        map(lambda x: x.strip(','), args)
        await ctx.send(f'**{random.choice(args)}**')

    def cleanup_code(self, content):
        # Remove ```py\n```.
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # Remove `foo`.
        return content.strip('` \n')

    # CRED: @Rapptz (https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/admin.py#L216)
    @commands.command(name='eval', pass_context=True)
    async def _eval(self, ctx, *, body: str):
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

    @commands.command(aliases=['coin_flip', 'heads', 'tails'])
    async def flip_coin(self, ctx, amount=1):
        """Flips coins."""
        if amount >= SPAM_LIMIT:
            raise exceptions.SpamError

        for _ in range(amount):
            await ctx.send(f'**{random.choice(["Heads", "Tails"])}**')

    @commands.command(aliases=['prefix'])
    async def get_prefix(self, ctx):
        """Gets the server's prefix."""
        file = open('bot/configs/prefixes.json')
        p = json.load(file)[str(ctx.message.guild.id)]
        await ctx.send(f'This server\'s prefix is `{p}`.')

    # frogges#1517 <@519950654555553806> challenged me to make this.
    # CRED: @Tortoise-Community (https://github.com/Tortoise-Community/Tortoise-BOT/blob/master/bot/cogs/utility.py#L19)
    # CAVEAT: Google's Custom Search JSON API provides only 100 search queries per day for free.
    @commands.command()
    async def google(self, ctx, *, query='query'):
        """Searches Google for a query."""
        pages = []

        await ctx.trigger_typing()
        results = await self.google_client.search(query)
        i = 1

        for result in results:
            embed = discord.Embed(title=result.title, description=result.description, url=result.url, colour=COLOUR)
            embed.set_thumbnail(url=result.image_url)
            # TODO: Should be handled by paginator. <@Tortoise-Community>
            embed.set_footer(text=f'Requested by {ctx.author.display_name} | Page {i}/{len(results)} | {query}',
                             icon_url=ctx.author.avatar_url)

            pages.append(embed)
            i += 1

        paginator = ListPaginator(ctx, pages)
        await paginator.start()

    @commands.command(aliases=['vote'])
    async def poll(self, ctx, *, question):
        """Creates a basic yes/no poll."""
        embed = discord.Embed(title='Poll', description=question, colour=COLOUR)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        message = await ctx.send(embed=embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷')

    @commands.command(aliases=['poll_num'])
    async def pollnum(self, ctx, *, question):
        """Creates a basic poll with numbers."""
        embed = discord.Embed(title='Poll', description=question, colour=COLOUR)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        message = await ctx.send(embed=embed)
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')

    @commands.command()
    async def translate(self, ctx, source=None, destination=None, *, query=None):
        """Translate text into a language.

        The source and destination languages are language codes.
        Type `?translate` to fetch all valid language codes.
        """
        if not (source and destination and query):
            # Fetch all valid language codes.
            pages = []

            codes = [f'{language} – `{code}`\n' for code, language in LANGUAGE_CODES.items()]
            code_list = ['']
            i = 1

            for code in codes:
                # Join up the codes into bigger blocks.
                if code_list[-1].count('\n') >= 20:
                    code_list.append('')
                code_list[-1] += code

            for codes in code_list:
                embed = discord.Embed(title='Language Codes', description=codes, colour=COLOUR)
                embed.set_footer(text=f'Requested by {ctx.author.display_name} | Page {i}/{len(code_list)}',
                                 icon_url=ctx.author.avatar_url)

                pages.append(embed)
                i += 1

            paginator = ListPaginator(ctx, pages)
            await paginator.start()
        else:
            source = source.lower()
            destination = destination.lower()

            if (source or destination) not in LANGUAGE_CODES.keys():
                await ctx.send('Invalid language code.')
            else:
                await ctx.trigger_typing()
                translation = self.translator.translate(query, dest=destination, src=source)

                embed = discord.Embed(title='Translate', colour=COLOUR)
                embed.add_field(name=LANGUAGE_CODES[source] + ':', value=translation.origin, inline=False)
                embed.add_field(name=LANGUAGE_CODES[destination] + ':', value=translation.text, inline=False)
                embed.set_footer(text=f'Requested by {ctx.author.display_name} | Powered by Google Translate',
                                 icon_url=ctx.author.avatar_url)

                await ctx.send(embed=embed)

    @commands.command(aliases=['dice', 'randint'])
    async def roll(self, ctx, *, b: int = 20, amount: int = 1):
        """Rolls the given number-sided dice."""
        if b < 1:
            await ctx.send('Please enter a non-negative whole number.')
            return
        if amount >= SPAM_LIMIT:
            raise exceptions.SpamError

        for _ in range(amount):
            await ctx.send(f'**{random.randint(1, b)}**')

    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please enter a non-negative whole number.')

    @commands.command(aliases=['dict', 'dictionary'])
    async def wiktionary(self, ctx, language, *, query):
        """Search a word on Wiktionary."""
        await ctx.trigger_typing()
        results = self.parser.fetch(query, language)

        try:
            top_word = results[0]
            top_definition = top_word['definitions'][0]
        except IndexError:
            await ctx.send('Sorry. I couldn\'t find that word.')
            return

        definition = top_definition['text'][0]
        i = 1

        for line in top_definition['text'][1:]:
            definition += f'\n    {i}. {line}'
            i += 1

        pronunciation = '\n'.join(top_word['pronunciations']['text']) or None
        etymology = top_word['etymology'][:300] or None
        part_of_speech = top_definition['partOfSpeech'].title()
        definition = definition[:1000]

        embed = discord.Embed(title=query, url=f'https://en.wiktionary.com/wiki/{query}', colour=COLOUR)

        if pronunciation:
            embed.add_field(name='Pronunciation', value=pronunciation, inline=False)
        if etymology:
            embed.add_field(name='Etymology', value=etymology, inline=False)

        embed.add_field(name=part_of_speech, value=definition, inline=False)
        embed.set_footer(text=f'Requested by {ctx.author.display_name} | Powered by Wiktionary',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utils(bot))
