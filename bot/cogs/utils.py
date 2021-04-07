import io
import json
import random
import textwrap
import traceback
from contextlib import redirect_stdout

import discord
from async_cse import Search
from discord.ext import commands
from googletrans import Translator
from wiktionaryparser import WiktionaryParser
from youtube_search import YoutubeSearch

from ..configs.configs import GOOGLE_API_KEY
from ..utils import exceptions
from ..utils.constants import COLOUR, SPAM_LIMIT
from ..utils.paginator import ListPaginator

LANGUAGES = json.load(open('bot/assets/text/language_codes.json'))
LANG_CODES = {v: k for k, v in LANGUAGES.items()}


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

    # CRED: @Tortoise-Community (https://github.com/Tortoise-Community/Tortoise-BOT/blob/master/bot/cogs/utility.py#L19)
    # NOTE: Google's Custom Search JSON API provides only 100 search queries per day for free.
    @commands.command()
    async def google(self, ctx, *, query):
        """Searches Google for a query."""
        page_list = []

        await ctx.trigger_typing()
        results = await self.google_client.search(query)
        i = 1

        for result in results:
            embed = discord.Embed(title=result.title, description=result.description, url=result.url, colour=COLOUR)
            embed.set_thumbnail(url=result.image_url)
            # TODO: Should be handled by paginator. <@Tortoise-Community>
            embed.set_footer(text=f'Requested by {ctx.author.display_name} | Page {i}/{len(results)} | {query}',
                             icon_url=ctx.author.avatar_url)

            page_list.append(embed)
            i += 1

        paginator = ListPaginator(ctx, page_list)
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
        -message = await ctx.send(embed=embed)
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')

    @commands.command(aliases=['gt'])
    async def translate(self, ctx, source=None, destination=None, *, query=None):
        """Translate text into a language.

        The source and destination languages are language codes.
        Type `?translate` to fetch all valid language codes.
        """
        if not (source and destination and query):
            # Fetch all valid language codes.
            page_list = []

            await ctx.trigger_typing()
            codes = sorted([f'{language} – `{code}`\n' for language, code in LANG_CODES.items()])
            code_list = ['']
            i = 1

            # Join up the codes into bigger chunks.
            for code in codes:
                if code_list[-1].count('\n') >= 20:
                    code_list.append('')
                code_list[-1] += code

            for codes in code_list:
                embed = discord.Embed(title='Language Codes', description=codes, colour=COLOUR)
                embed.set_footer(text=f'Requested by {ctx.author.display_name} | Page {i}/{len(code_list)}',
                                 icon_url=ctx.author.avatar_url)

                page_list.append(embed)
                i += 1

            paginator = ListPaginator(ctx, page_list)
            await paginator.start()
        else:
            source = source.lower()
            destination = destination.lower()

            if source not in LANGUAGES.keys() or destination not in LANGUAGES.keys():
                await ctx.send('Invalid language code(s).')
                return

            await ctx.trigger_typing()
            try:
                translation = self.translator.translate(query, dest=destination, src=source)
            except TypeError:
                await ctx.send('Something went wrong while translating.')
                return

            translated_text = translation.text

            if translation.pronunciation:
                if not isinstance(translation.pronunciation, str):
                    pass
                elif (translation.pronunciation == translation.origin
                        or translation.pronunciation == translation.text):
                    pass
                else:
                    translated_text += f'\n({translation.pronunciation})'

            embed = discord.Embed(title='Translate', colour=COLOUR)
            embed.add_field(name=LANGUAGES[source] + ':', value=translation.origin, inline=False)
            embed.add_field(name=LANGUAGES[destination] + ':', value=translated_text, inline=False)
            embed.set_footer(text=f'Requested by {ctx.author.display_name} | Powered by Google Translate',
                             icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

    @commands.command(aliases=['dice', 'randint'])
    async def roll(self, ctx, faces: int = 20, amount: int = 1):
        """Rolls the number-sided dice."""
        if faces < 1:
            await ctx.send('Please enter a non-negative whole number.')
            return
        if amount >= SPAM_LIMIT:
            raise exceptions.SpamError

        for _ in range(amount):
            await ctx.send(f'**{random.randint(1, faces)}**')

    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please enter a non-negative whole number.')

    @commands.command(aliases=['dict', 'dictionary', 'wikt'])
    async def wiktionary(self, ctx, language, *, query):
        """Search Wiktionary for a query."""
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

        embed = discord.Embed(title=query, url=f'https://en.wiktionary.org/wiki/{query.replace(" ", "_")}'
                              f'#{language.title().replace(" ", "_")}', colour=COLOUR)

        if pronunciation:
            embed.add_field(name='Pronunciation', value=pronunciation, inline=False)
        if etymology:
            embed.add_field(name='Etymology', value=etymology, inline=False)

        embed.add_field(name=part_of_speech, value=definition, inline=False)
        embed.set_footer(text=f'Requested by {ctx.author.display_name} | Powered by Wiktionary',
                         icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def youtube(self, ctx, *, query):
        """Search YouTube for a query."""
        try:
            page_list = []

            await ctx.trigger_typing()
            results = YoutubeSearch(query, max_results=20).to_dict()
            i = 1

            for result in results:
                embed = discord.Embed(title=result['title'], description=result['long_desc'],
                                      url=f'https://youtu.be/{result["id"]}', colour=COLOUR)
                embed.set_thumbnail(url=result['thumbnails'][0])
                embed.set_footer(text=f'Requested by {ctx.author.display_name} | Page {i}/{len(results)} | {query}',
                                 icon_url=ctx.author.avatar_url)

                page_list.append(embed)
                i += 1

            paginator = ListPaginator(ctx, page_list)
            await paginator.start()
        except Exception as e:
            traceback_msg = ''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__))
            await ctx.send(f'Traceback:\n```{traceback_msg}```')


def setup(bot):
    bot.add_cog(Utils(bot))
