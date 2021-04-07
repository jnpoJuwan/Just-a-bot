import random
from typing import Union

import discord
from discord.ext import commands


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def get_names(member_or_roles, is_genitive=False):
        name_list = []

        for obj in member_or_roles:
            if isinstance(obj, discord.Member):
                name = obj.display_name
            elif isinstance(obj, discord.Role):
                name = obj.name
            else:
                name = obj

            if is_genitive:
                name_list.append(name + '\'' if name.lower().endswith('s') else name + '\'s')
            else:
                name_list.append(name)

        return name_list

    def add_list_formatting(self, members_or_roles=None, is_genitive=False):
        if not members_or_roles:
            return

        members_or_roles = self.get_names(members_or_roles, is_genitive)

        if len(members_or_roles) == 1:
            return members_or_roles[0]
        elif len(members_or_roles) == 2:
            return members_or_roles[0] + ' and ' + members_or_roles[1]
        else:
            return ', '.join(members_or_roles[:-1]) + ' and ' + members_or_roles[-1]

    async def interact(self, ctx, messages, members=None):
        if not members:
            if isinstance(messages[0], discord.File):
                await ctx.send(file=messages[0])
            else:
                await ctx.send(messages[0])
        elif members[0] == ctx.author:
            await ctx.send(messages[1])
        elif members[0] == self.bot.user:
            await ctx.send(messages[2])
        else:
            await ctx.send(messages[3])
            for member in members:
                try:
                    await member.send(messages[4])
                except discord.HTTPException:
                    pass

    @commands.command(aliases=['bigcuddle'])
    async def big_cuddle(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Cuddles someone."""
        messages = [
            'You gave your pillow cuddles and lots of love, since you\'re alone and lonely.',
            'You gave yourself cuddles and lots of love.',
            'You gave me cuddles and lots of love. 🥺 💖',
            f'You gave {self.add_list_formatting(members_or_roles)} a long intensive cuddle with a lots of love. 💖',
            f'{ctx.author.name} gave you cuddles and lots of love. 💖'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def bonk(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Bonks someone."""
        messages = [
            'You didn\'t bonk anyone.',
            'You bonked yourself to horny jail.',
            'You bonked me to horny jail.',
            f'You bonked {self.add_list_formatting(members_or_roles)} to horny jail.',
            f'{ctx.author.name} bonk you to horny jail.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def cuddle(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Cuddles someone."""
        messages = [
            'You cuddled your pillow, since you\'re alone and lonely.',
            'You cuddled yourself.',
            'You cuddled me. 🥺',
            f'You cuddled {self.add_list_formatting(members_or_roles)}.',
            f'{ctx.author.name} cuddled you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=["cri"])
    async def cry(self, ctx):
        """Cries."""
        image = discord.File(open('bot/assets/images/cry.jpg', 'rb'))
        await ctx.send('<:cat_cry:814925690528333885>', file=image)

    @commands.command(aliases=['ejaculate', 'cream', 'jizz', 'nut', 'sperm', 'splooge'])
    async def cum(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Cums or creams someone."""
        messages = [
            'Oopsie-doopsie! You cummed all over yourself!',
            'You creamed yourself.',
            'You want to c-cum inside my tiny robot bussy, master? 🥺',
            f'You creamed {self.add_list_formatting(members_or_roles, is_genitive=True)} little þussy. '
            f'You\'re under arrest to horny jail.',
            f'{ctx.author.name} creamed you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['dnace'])
    async def dance(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Dance with someone."""
        messages = [
            'You *dnaced*.',
            'You danced with yourself.',
            'You danced with me.',
            f'You danced with {self.add_list_formatting(members_or_roles)}.',
            f'{ctx.author.name} danced with you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def frost(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Frosts someone."""
        messages = [
            discord.File(open('bot/assets/images/frost.png', 'rb')),
            'You frosted yourself like a birthday cake.',
            'You frosted me like a birthday cake.',
            f'You frosted {self.add_list_formatting(members_or_roles, is_genitive=True)} like a birthday cake.',
            f'{ctx.author.name} frosted you like a birthday cake.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['fuq', 'fwk', 'destroy', 'sex'])
    async def fuck(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Fucks someone."""
        messages = [
            'You fucked your pillow, since you\'re alone and lonely, and officially became PD6.',
            'You self-fucked.',
            'You fucked my tiny robot bussy. 🥺',
            f'You fucked tiny {self.add_list_formatting(members_or_roles, is_genitive=True)} þussy.'
            f'You\'re under arrest to horny jail.',
            f'{ctx.author.name} fucked your tiny þussy.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['hand_hold', 'hold_hands'])
    async def hold_hand(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Holds hands with someone."""
        messages = [
            'You didn\'t hold anybody\'s hand.',
            'You held your own hand, since you\'re alone and lonely.',
            'You held my tiny robot hand. 🥺',
            f'You held {self.add_list_formatting(members_or_roles, is_genitive=True)} hand. 😳 👉👈',
            f'{ctx.author.name} held your hand.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def hug(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Hugs someone."""
        messages = [
            'You hugged your pillow, since you\'re alone and lonely.',
            'You hugged yourself.',
            'You hugged me. 🥺',
            f'You hugged {self.add_list_formatting(members_or_roles)}.',
            f'{ctx.author.name} hugged you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['assassinate', 'murder', 'slaughter'])
    async def kill(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Brutally kills someone."""
        messages = [
            'You didn\'t kill anyone.',
            '<:gunpoint:804365552801677312> <:cry2:825451191345348648>',
            'But m-master... \\*is brutally killed\\*',
            f'You have murdered {self.add_list_formatting(members_or_roles)}. You\'re now on MAGNVS\' wanted list.',
            f'{ctx.author.name} killed you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def kiss(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Kisses someone."""
        messages = [
            'You kissed your pillow, since you\'re alone and lonely.',
            'You kissed yourself.',
            'You kissed me, master. 🥺',
            f'You kissed {self.add_list_formatting(members_or_roles)}. 😳 👉👈',
            f'{ctx.author.name} kissed you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def love(self, ctx):
        """Love ❤️ 💕."""
        image = discord.File(open('bot/assets/images/love.jpg', 'rb'))
        await ctx.send('❤️ 💕', file=image)

    @commands.command()
    async def moan(self, ctx):
        """Moans."""
        image = discord.File(open('bot/assets/images/moan.png', 'rb'))
        await ctx.send('And this guy moaned at least this loud.', file=image)

    @commands.command(aliases=['headpat'])
    async def pat(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Pats someone on the head."""
        messages = [
            'You patted your pillow, since you\'re alone and lonely.',
            'You patted yourself.',
            'You patted me. 🥺',
            f'You patted {self.add_list_formatting(members_or_roles)} on the head.',
            f'{ctx.author.name} patted you on the head.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def poke(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Pokes someone."""
        messages = [
            'You poked your pillow, since you\'re alone and lonely.',
            'You poked yourself.',
            'You poked me.',
            f'You poked {self.add_list_formatting(members_or_roles)}.',
            f'{ctx.author.name} poked you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def punish(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Punishes someone."""
        messages = [
            'You didn\'t punish anyone.',
            'You punished yourself for being naughty.',
            'You punished me for being naughty.',
            f'You punished {self.add_list_formatting(members_or_roles)} for being naughty.',
            f'{ctx.author.name} punished you for being naughty.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def reject(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role, str]] = None):
        """Rejects someone."""
        # Fin#2372 (<@443551308692062209>) requested the feature to reject strings of text
        # (e.g. ?reject capitalism).
        messages = [
            'You didn\'t reject anyone.',
            'You rejected yourself. <:noooooooo:809935851052072980>',
            'You rejected me. <:cry2:825451191345348648>',
            f'You rejected {self.add_list_formatting(members_or_roles)}.',
            f'{ctx.author.name} rejected you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def scream(self, ctx):
        """Screams."""
        file = open('bot/assets/images/scream.jpg', 'rb')
        image = discord.File(file)
        await ctx.send(file=image)

    @commands.command()
    async def shoot(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Shoots someone."""
        messages = [
            'You didn\'t shoot anyone.',
            '<:gunpoint:804365552801677312> <:cry2:825451191345348648>',
            'But m-master... \\*gets shot\\*',
            f'You shot {self.add_list_formatting(members_or_roles)}.',
            f'{ctx.author.name} shot you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def shy_hug(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Shyly hugs someone."""
        messages = [
            'You hugged your pillow, since you\'re alone and lonely.',
            'You hugged yourself.',
            'You hugged me. 🥺 👉👈',
            f'You hugged {self.add_list_formatting(members_or_roles)}. 😳 👉👈',
            f'{ctx.author.name} hugged you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def slap(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Slaps someone's face or their thicc, juicy arse."""
        choices = [
            ['You facepalmed.',
             'You facepalmed.',
             'You slapped me. <:cry2:825451191345348648>',
             f'You slapped {self.add_list_formatting(members_or_roles)}.',
             f'{ctx.author.name} slapped you.'],

            ['You slapped your own thicc arse',
             'You slapped your own thicc arse',
             'You slapped my robot arse.',
             f'You slapped {self.add_list_formatting(members_or_roles)}\'s thicc arse.',
             f'{ctx.author.name} slapped your thicc arse.']
        ]
        messages = random.choice(choices)

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def stab(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Stabs someone."""
        messages = [
            'You didn\'t stab anyone.',
            '<:gunpoint:804365552801677312> <:cry2:825451191345348648>',
            '\\*gets stabbed 23 times\\* Et tu, dominus? \\*dies\\*.',
            f'You brutally stabbed {self.add_list_formatting(members_or_roles)}.',
            f'{ctx.author.name} stabbed your heart.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['suq'])
    async def suck(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Sucks someone off."""
        messages = [
            discord.File(open('bot/assets/images/suck.png', 'rb')),
            'You self-sucked.',
            'You sucked my tiny cock.',
            f'You sucked {self.add_list_formatting(members_or_roles)}. You\'re under arrest to horny jail.',
            f'{ctx.author.name} sucked you.'
        ]

        await self.interact(ctx, messages, members_or_roles)


def setup(bot):
    bot.add_cog(Actions(bot))
