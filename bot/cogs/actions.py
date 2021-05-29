import random

import discord
from discord.ext import commands
from typing import Union


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
                if obj.name == '@everyone':
                    name = '@\u200beveryone'
                else:
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

    async def interact(self, ctx, messages, members_or_roles=None):
        if not members_or_roles:
            if isinstance(messages[0], discord.File):
                await ctx.send(file=messages[0])
            else:
                await ctx.send(messages[0])
        elif members_or_roles[0] == ctx.author:
            await ctx.send(messages[1])
        elif members_or_roles[0] == self.bot.user:
            await ctx.send(messages[2])
        else:
            await ctx.send(messages[3])

    @commands.command(aliases=['bigcuddle'])
    async def big_cuddle(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Gives someone a big cuddle."""
        messages = [
            'You gave your pillow cuddles and lots of love, since you\'re alone and lonely.',
            'You gave yourself cuddles and lots of love.',
            'You gave me cuddles and lots of love. 🥺 💖',
            f'You gave {self.add_list_formatting(members_or_roles)} a long intensive cuddle with a lots of love. 💖',
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
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def christ(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Cums or creams someone."""
        liquid = random.choice(['holy water', 'wine'])
        messages = [
            f'Oopsie-woopsie! You cummed {liquid}!',
            f'You blessed yourself with your {liquid}.',
            f'You want to bless my tiny, robot bussy with your {liquid}, master? 🥺',
            f'You blessed {self.add_list_formatting(members_or_roles, is_genitive=True)} little þussy with {liquid}.',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=["cri"])
    async def cry(self, ctx):
        """Cries."""
        image = discord.File(open('bot/assets/images/cry.jpg', 'rb'))
        await ctx.send('<:cat_cry:814925690528333885>', file=image)

    @commands.command()
    async def cuddle(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Cuddles someone."""
        messages = [
            'You cuddled your pillow, since you\'re alone and lonely.',
            'You cuddled yourself.',
            'You cuddled me. 🥺',
            f'You cuddled {self.add_list_formatting(members_or_roles)}.',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['ejaculate', 'cream', 'jizz', 'goo', 'nut', 'sperm', 'splooge', 'splurt'])
    async def cum(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Cums or creams someone."""
        messages = [
            'Oopsie-woopsie! You cummed all over yourself!',
            'You creamed yourself.',
            'You want to c-cum inside my tiny, robot bussy, master? 🥺',
            f'You creamed {self.add_list_formatting(members_or_roles, is_genitive=True)} little þussy.',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['cwtsh'])
    async def cwtch(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Cwtches someone."""
        messages = [
            'You cwtched your pillow in your arms, since you\'re alone and lonely.',
            'You cwtched yourself. 💕',
            'You cwtched me. 🥺 💕',
            f'You cwtched {self.add_list_formatting(members_or_roles)} in your arms. 💕',
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
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['destroy', 'frick', 'fuq', 'fwk', 'sex'])
    async def fuck(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Fucks someone."""
        messages = [
            'You fucked your pillow, since you\'re alone and lonely, and officially became PD6.',
            'You went fuck yourself as someone asked.',
            'You fucked my tiny, robot bussy. 🥺',
            f'You fucked {self.add_list_formatting(members_or_roles, is_genitive=True)} tiny þussy.',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['hand_hold', 'hold_hands'])
    async def hold_hand(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Holds hands with someone."""
        messages = [
            'You didn\'t hold anybody\'s hand.',
            'You held your own hand, since you\'re alone and lonely.',
            'You held my tiny, robot hand. 🥺',
            f'You held {self.add_list_formatting(members_or_roles, is_genitive=True)} hand. 😳 👉👈',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def hug(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Hugs someone."""
        messages = [
            'You hugged your pillow, since you\'re alone and lonely.',
            'You hugged yourself. 💕',
            'You hugged me. 🥺 💕',
            f'You hugged {self.add_list_formatting(members_or_roles)}. 💕',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['jerk'])
    async def jerk_off(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Jerkes someone off."""
        messages = [
            'You jerked off, since you\'re alone and lonely.',
            'You jerked yourself off.',
            'You jerked me off.',
            f'You jerked {self.add_list_formatting(members_or_roles)} off.',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['assassinate', 'murder', 'slaughter'])
    async def kill(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Brutally kills someone."""
        messages = [
            'You didn\'t kill anyone.',
            '<:gunpoint:804365552801677312> <:cry2:829114403961438249>',
            'But m-master... \\*is brutally killed\\*',
            f'You have murdered {self.add_list_formatting(members_or_roles)}. You\'re now on MAGNVS\' wanted list.',
        ]

        if 362602502644039691 in [member.id for member in members_or_roles]:
            await ctx.send('You cannot kill MAGNVS. He is immortal.')
        else:
            await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['kissie'])
    async def kiss(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Kisses someone."""
        messages = [
            'You kissed your pillow, since you\'re alone and lonely.',
            'You kissed yourself.',
            'You kissed me, master. 🥺',
            f'You kissed {self.add_list_formatting(members_or_roles)}. 😳 👉👈',
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

    @commands.command(aliases=['headpat', 'pet'])
    async def pat(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Pats someone on the head."""
        messages = [
            'You patted your pillow, since you\'re alone and lonely.',
            'You patted yourself.',
            'You patted me. 🥺',
            f'You patted {self.add_list_formatting(members_or_roles)} on the head.',
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
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def reject(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role, str]] = None):
        """Rejects someone."""
        # Someone requested the feature to reject strings of text, for example ?reject capitalism.
        messages = [
            'You didn\'t reject anyone.',
            'You rejected yourself. <:noooooooo:809935851052072980>',
            'You rejected me. <:cry2:829114403961438249>',
            f'You rejected {self.add_list_formatting(members_or_roles)}.',
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
            '<:gunpoint:804365552801677312> <:cry2:829114403961438249>',
            'But m-master... \\*gets shot\\*',
            f'You shot {self.add_list_formatting(members_or_roles)}.',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def shy_hug(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Shyly hugs someone."""
        messages = [
            'You shyly hugged your pillow, since you\'re alone and lonely. 💕',
            'You shyly hugged yourself. 💕',
            'You shyly hugged me. 🥺 👉👈',
            f'You shyly hugged {self.add_list_formatting(members_or_roles)}. 😳 👉👈',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['smack'])
    async def slap(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Slaps someone."""
        messages = [
            'You slapped your pillow, since you\'re alone and lonely.',
            'You slapped yourself in the face.',
            'You slapped me. <:cry2:829114403961438249>',
            f'You slapped {self.add_list_formatting(members_or_roles)} in the face.',
         ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def spank(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Spanks someone."""
        messages = [
            'You didn\'t spank anyone.',
            'You spanked yourself.',
            'You spanked my robot arse. 😳',
            f'You spanked {self.add_list_formatting(members_or_roles, is_genitive=True)} cute arse.',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def stab(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Stabs someone."""
        messages = [
            'You didn\'t stab anyone.',
            '<:gunpoint:804365552801677312> <:cry2:829114403961438249>',
            '\\*gets stabbed 23 times\\* Et tu, dominus? \\*dies\\*.',
            f'You brutally stabbed {self.add_list_formatting(members_or_roles)}.',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['suq'])
    async def suck(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Sucks someone off."""
        messages = [
            discord.File(open('bot/assets/images/suck.png', 'rb')),
            'You self-sucked.',
            'You sucked my tiny, robot cock. 😳',
            f'You sucked {self.add_list_formatting(members_or_roles, is_genitive=True)} monster cock. 😳',
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['3some'])
    async def threesome(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Has a threesome with some people."""
        if not members_or_roles:
            await ctx.send('Dude, do you want a hug? <:cry2:829114403961438249>')
        elif len(members_or_roles) == 1:
            await ctx.send(f'You had a threesome with {self.add_list_formatting(members_or_roles)} and your pillow.')
        elif len(members_or_roles) == 2:
            await ctx.send(f'You had a threesome with {self.add_list_formatting(members_or_roles[:2])}.')
        else:
            await ctx.send(f'You had a threesome with {self.add_list_formatting(members_or_roles[:2])} and '
                           f'{self.add_list_formatting(members_or_roles[2:])} watched you doing the naughties.')


def setup(bot):
    bot.add_cog(Actions(bot))
