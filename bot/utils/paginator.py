import asyncio
from typing import List, Union

import discord
from discord.abc import Messageable
from discord.ext import commands

from .constants import COLOUR, TIMEOUT, ARROW_TO_BEGINNING, LEFT_ARROW, DELETE_EMOJI, RIGHT_ARROW, ARROW_TO_END, \
    PAGINATION_EMOJI


# CRED: @Tortoise-Community (https://github.com/Tortoise-Community/Tortoise-BOT/blob/master/bot/utils/paginator.py)
class Paginator:
    def __init__(
            self, *,
            page_size: int = 2000,
            separator: str = '\n',
            timeout: int = TIMEOUT,
            prefix: str = '',
            suffix: str = ''
    ):
        """
        :param page_size: Maximum page string size for the page content.
        :param separator: Separator used to break large chunks of content to smaller ones, if needed.
        :param timeout: How long will the reactions be awaited for.
        :param prefix: Prefix for the message content.
        :param suffix: Suffix for the message content.
        """
        self._separator = separator
        self._timeout = timeout
        self._prefix = prefix
        self._suffix = suffix
        self._message = None
        self._page_index = 0
        self._content = []
        self._pages = []
        self._max_page_size = page_size - len(self.prefix) - len(self.suffix)

    def _make_pages(self):
        pages = []
        chunks = self.content.split(self._separator)
        self.break_long_entries(chunks, self._max_page_size)

        temp_page = []
        for entry in chunks:
            # len(temp_chunk) is because we'll add separators in join.
            if sum(map(len, temp_page)) + len(entry) + len(temp_page) >= self._max_page_size:
                pages.append(self._separator.join(temp_page))
                temp_page = [entry]
            else:
                temp_page.append(entry)

        # For leftovers.
        pages.append(self._separator.join(temp_page))
        return pages

    @staticmethod
    def break_long_entries(chunk_list: List[str], max_chunk_size: int):
        """
        We further break down chunk_list in case any of the entries are larger than max_chunk_size.
        Modifies passed list in place!
        Will throw RecursionError if the string length in list is mega-huge.
        Basically when the entry is found just split it in half and re-add it in list without breaking order.
        Split in half will be done as many times as needed as long as resulting entry is larger than max_chunk_size
        :param chunk_list: list of strings
        :param max_chunk_size: integer, if chunk is larger that this we break it down
        """
        for i, entry in enumerate(chunk_list):
            if len(entry) > max_chunk_size:
                # Split string in 2 parts by the middle.
                f, s = entry[:len(entry) // 2], entry[len(entry) // 2:]
                # Append them back to our list, not breaking order.
                chunk_list[i] = s
                chunk_list.insert(i, f)
                # Keep doing that until there is no entries that are larger in length than max_msg_size.
                Paginator.break_long_entries(chunk_list, max_chunk_size)
                break

    async def start(self, destination: Messageable, author: Union[discord.User, discord.Member], bot_reference):
        self._pages = self._make_pages()
        await self.create_message(destination)
        if len(self._pages) > 1:
            # No need to paginate if there are no pages.
            await self._add_all_reactions()
            await self._start_listener(author, bot_reference)

    def close_page(self):
        # Just to condone to standard paginator.
        pass

    @property
    def prefix(self):
        return self._prefix

    @property
    def suffix(self):
        return self._suffix

    @property
    def max_size(self):
        return self._max_page_size

    @property
    def pages(self):
        return self._pages

    @property
    def content(self):
        return ''.join(self._content)

    def clear(self):
        self._pages = []
        self._page_index = 0

    def add_line(self, line: str = '', **kwargs):
        self._content.append(line)

    def _get_page_counter_message(self):
        return f'Page {self._page_index + 1}/{len(self._pages)}'

    async def _add_all_reactions(self):
        for emoji in PAGINATION_EMOJI:
            await self._message.add_reaction(emoji)

    async def clear_all_reactions(self):
        try:
            await self._message.clear_reactions()
        except discord.HTTPException:
            pass

    async def create_message(self, destination: Messageable):
        self._message = await destination.send(self.get_message_content())

    async def update_message(self):
        await self._message.edit(content=self.get_message_content())

    def get_message_content(self):
        return f'{self.prefix}{self._pages[self._page_index]}{self.suffix}'

    async def _remove_reaction(self, reaction, author: Union[discord.User, discord.Member]):
        try:
            await self._message.remove_reaction(reaction, author)
        except discord.HTTPException:
            pass

    async def _start_listener(self, author: Union[discord.User, discord.Member], bot_reference):
        def check(reaction_, user_):
            return (
                    str(reaction_) in PAGINATION_EMOJI and
                    user_.id == author.id and
                    reaction_.message.id == self._message.id
            )

        while True:
            try:
                reaction, user = await bot_reference.wait_for('reaction_add', timeout=self._timeout, check=check)
            except asyncio.TimeoutError:
                await self.clear_all_reactions()
                break

            if str(reaction) == ARROW_TO_BEGINNING:
                await self._remove_reaction(ARROW_TO_BEGINNING, author)
                if self._page_index > 0:
                    self._page_index = 0
                    await self.update_message()
            elif str(reaction) == LEFT_ARROW:
                await self._remove_reaction(LEFT_ARROW, author)
                if self._page_index > 0:
                    self._page_index -= 1
                    await self.update_message()
            elif str(reaction) == DELETE_EMOJI:
                return await self._message.delete()
            elif str(reaction) == RIGHT_ARROW:
                await self._remove_reaction(RIGHT_ARROW, author)
                if self._page_index < len(self._pages) - 1:
                    self._page_index += 1
                    await self.update_message()
            elif str(reaction) == ARROW_TO_END:
                await self._remove_reaction(ARROW_TO_END, author)
                if self._page_index < len(self._pages) - 1:
                    self._page_index = len(self._pages) - 1
                    await self.update_message()


class EmbedPaginator(Paginator):
    def __init__(self, embed_title='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._embed_title = embed_title

    @classmethod
    def _get_bot_member_from_destination(cls, destination: Messageable):
        try:
            # noinspection PyUnresolvedReferences
            return destination.guild.me
        except AttributeError:
            # noinspection PyUnresolvedReferences
            return destination.me

    async def create_message(self, destination):
        embed = discord.Embed(title=self._embed_title, description=self.get_message_content(), colour=COLOUR)
        embed.set_footer(text=self._get_page_counter_message())
        self._message = await destination.send(embed=embed)

    async def update_message(self):
        embed = discord.Embed(title=self._embed_title, description=self.get_message_content(), colour=COLOUR)
        embed.set_footer(text=self._get_page_counter_message())
        await self._message.edit(embed=embed)


class ListPaginator:
    """Constructs a paginator when provided a list of embeds/messages."""
    def __init__(self, ctx: commands.Context, page_list):
        self.pages = page_list
        self.ctx = ctx
        self.bot = ctx.bot

    def get_next_page(self, page):
        pages = self.pages

        if page != pages[-1]:
            current_page_index = pages.index(page)
            next_page = pages[current_page_index+1]
            return next_page

        return pages[-1]

    def get_prev_page(self, page):
        pages = self.pages

        if page != pages[0]:
            current_page_index = pages.index(page)
            next_page = pages[current_page_index-1]
            return next_page

        return pages[0]

    async def start(self):
        ctx = self.ctx
        pages = self.pages
        embed = pages[0]
        msg = await ctx.send(embed=embed)

        for emote in PAGINATION_EMOJI:
            await msg.add_reaction(emote)

        def check(_reaction, _user):
            return _user == ctx.author and str(_reaction.emoji) in PAGINATION_EMOJI and _reaction.message == msg

        current_page = embed

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=TIMEOUT, check=check)

                if str(reaction.emoji) == ARROW_TO_BEGINNING:
                    await msg.edit(embed=pages[0])
                    current_page = pages[0]
                    await msg.remove_reaction(ARROW_TO_BEGINNING, ctx.author)

                elif str(reaction.emoji) == ARROW_TO_END:
                    await msg.edit(embed=pages[-1])
                    current_page = pages[-1]
                    await msg.remove_reaction(ARROW_TO_END, ctx.author)

                elif str(reaction.emoji) == RIGHT_ARROW:
                    next_page = self.get_next_page(current_page)
                    await msg.edit(embed=self.get_next_page(current_page))
                    current_page = next_page
                    await msg.remove_reaction(RIGHT_ARROW, ctx.author)

                elif str(reaction.emoji) == DELETE_EMOJI:
                    await msg.delete()
                    break

                elif str(reaction.emoji) == LEFT_ARROW:
                    prev_page = self.get_prev_page(current_page)
                    await msg.edit(embed=prev_page)
                    current_page = prev_page
                    await msg.remove_reaction(LEFT_ARROW, ctx.author)
            except asyncio.TimeoutError:
                await msg.clear_reactions()
