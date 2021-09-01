from typing import Union

import discord
from discord.ext import commands


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def get_names(member_or_roles, gen=False):
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

            if gen:
                name_list.append(name + '\'s')
            else:
                name_list.append(name)

        return name_list

    def name_format(self, members_or_roles=None, gen=False):
        if not members_or_roles:
            return

        members_or_roles = self.get_names(members_or_roles, gen)

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
        elif len(members_or_roles) == 1:
            await ctx.send(messages[3])
        else:
            await ctx.send(messages[4])

    @commands.command(aliases=['bigcuddle'])
    async def big_cuddle(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Gives someone a big cuddle."""
        messages = [
            'You gave your pillow cuddles and lots of love, since you\'re alone and lonely.',
            'You gave yourself cuddles and lots of love.',
            'You gave me cuddles and lots of love. :pleading_face: 💖',
            f'You gave {self.name_format(members_or_roles)} a long, intensive cuddle full of love. :sparkling_heart:',
            f'You gave {self.name_format(members_or_roles)} long, intensive cuddles full of love. :sparkling_heart:'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def bonk(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Bonks someone."""
        if ctx.author.id == 616812057186271233:
            await ctx.send('No! Bad Eddie!')
            return

        messages = [
            'You didn\'t bonk anyone.',
            'You bonked yourself to horny jail.',
            'You bonked me to horny jail.',
            f'You bonked {self.name_format(members_or_roles)} to horny jail.',
            f'You bonked {self.name_format(members_or_roles)} to horny jail.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['cri'])
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
            'You cuddled me. :pleading_face:',
            f'You cuddled {self.name_format(members_or_roles)}.',
            f'You cuddled {self.name_format(members_or_roles)}.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['ejaculate', 'cream', 'jizz', 'goo', 'nut', 'sperm', 'splooge', 'splurt'])
    async def cum(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Cums or creams someone."""
        messages = [
            'Oopsie-woopsie! You cummed all over yourself!',
            'You creamed yourself.',
            'You want to c-cum inside my tiny, robot bussy, Master? :pleading_face:',
            f'You creamed {self.name_format(members_or_roles, gen=True)} little þussy.',
            f'You creamed {self.name_format(members_or_roles, gen=True)} little þussies.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['cwtsh'])
    async def cwtch(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Cwtches someone."""
        messages = [
            'You cwtched your pillow in your arms, since you\'re alone and lonely.',
            'You cwtched yourself. :two_hearts:',
            'You cwtched me. :pleading_face: :two_hearts:',
            f'You cwtched {self.name_format(members_or_roles)} in your arms. :two_hearts:',
            f'You cwtched {self.name_format(members_or_roles)} in your arms. :two_hearts:'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['dnace'])
    async def dance(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Dance with someone."""
        messages = [
            'You *dnaced*.',
            'You danced with yourself.',
            'You danced with me.',
            f'You danced with {self.name_format(members_or_roles)}.'
            f'You danced with {self.name_format(members_or_roles)}.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliasese=['throw', 'yeet'])
    async def defenestrate(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Throws someone out the window."""
        messages = [
            'You defenestrated your pillow.',
            'You defenestrated yourself.',
            'You defenestrated me.',
            f'You defenestrated {self.name_format(members_or_roles)}.'
            f'You defenestrated {self.name_format(members_or_roles)}.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def frost(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Frosts someone."""
        messages = [
            discord.File(open('bot/assets/images/frost.png', 'rb')),
            'You frosted yourself like a birthday cake.',
            'You frosted me like a birthday cake.',
            f'You frosted {self.name_format(members_or_roles, gen=True)} like a birthday cake.'
            f'You frosted {self.name_format(members_or_roles, gen=True)} like birthday cakes.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(
        aliases=['bang', 'breed', 'bone', 'coition', 'copulate', 'destroy', 'fill', 'frick', 'fornicate', 'fuq', 'fwk',
                 'lovemake', 'mate', 'penetrate', 'pound', 'rail', 'reproduce', 'screw', 'sex', 'shag', 'slay',
                 'smash', 'snoo_snoo', 'top']
    )
    async def fuck(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Fucks someone."""
        messages = [
            'You fucked your pillow, since you\'re alone and lonely... Do you need a hug?',
            'You went fuck yourself as someone asked.',
            'You fucked my tiny, robot bussy. :pleading_face:',
            f'You fucked {self.name_format(members_or_roles, gen=True)} tiny þussy.'
            f'You fucked {self.name_format(members_or_roles, gen=True)} tiny þussies.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['hand_hold', 'hold_hands'])
    async def hold_hand(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Holds hands with someone."""
        messages = [
            'You didn\'t hold anybody\'s hand.',
            'You held hands with yourself, since you\'re alone and lonely.',
            'You held my tiny, robot hand. :pleading_face:',
            f'You held hands with {self.name_format(members_or_roles)}. :flushed: :point_right::point_left:',
            f'You held hands with {self.name_format(members_or_roles)}. :flushed: :point_right::point_left:'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def hug(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Hugs someone."""
        messages = [
            'You hugged your pillow, since you\'re alone and lonely.',
            'You hugged yourself. :two_hearts:',
            'You hugged me. :pleading_face: :two_hearts:',
            f'You hugged {self.name_format(members_or_roles)}. :two_hearts:',
            f'You hugged {self.name_format(members_or_roles)}. :two_hearts:'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['fap', 'jerk', 'masturbate', 'milk'])
    async def jerk_off(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Jerkes someone off."""
        messages = [
            'You jerked off, since you\'re alone and lonely.',
            'You jerked yourself off.',
            'You jerked me off.',
            f'You jerked {self.name_format(members_or_roles)} off.',
            f'You jerked {self.name_format(members_or_roles)} off.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['assassinate', 'murder', 'slaughter'])
    async def kill(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Brutally kills someone."""
        messages = [
            'You didn\'t kill anyone.',
            '<:gunpoint:859930591265161216> <:cry2:829114403961438249>',
            'But M-master... \\*is brutally killed\\*',
            f'You have murdered {self.name_format(members_or_roles)}.',
            f'You have murdered {self.name_format(members_or_roles)}. You\'re a mass murderer now.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['kissie', 'kissy', 'kith'])
    async def kiss(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Kisses someone."""
        messages = [
            'You kissed your pillow, since you\'re alone and lonely.',
            'You kissed your reflection on the mirror like a narcissist',
            'You kissed me, Master. :pleading_face:',
            f'You kissed {self.name_format(members_or_roles)}. :flushed: :point_right::point_left:',
            f'You kissed {self.name_format(members_or_roles)}. :flushed: :point_right::point_left:'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def love(self, ctx):
        """Love. :heart: :two_hearts:"""
        image = discord.File(open('bot/assets/images/love.jpg', 'rb'))
        await ctx.send(':heart: :two_hearts:', file=image)

    @commands.command()
    async def moan(self, ctx):
        """Moans."""
        image = discord.File(open('bot/assets/images/moan.png', 'rb'))
        await ctx.send('And this guy moaned at least this loud.', file=image)

    @commands.command(aliases=['big_kiss', 'big_kissie', 'make_out', 'passion_kiss'])
    async def passionate_kiss(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Passionately kisses someone."""
        messages = [
            'You made out with your pillow, since you\'re alone and lonely.',
            'You made out with your reflection on the mirror like a narcissist.',
            'You made out with me, Master. :pleading_face:',
            f'You passionately kissed {self.name_format(members_or_roles)}. :flushed: :point_right::point_left:',
            f'You passionately kissed {self.name_format(members_or_roles)}. :flushed: :point_right::point_left:'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['headpat', 'pet'])
    async def pat(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Pats someone on the head."""
        messages = [
            'You patted your pillow, since you\'re alone and lonely.',
            'You patted yourself.',
            'You patted me. :pleading_face:',
            f'You patted {self.name_format(members_or_roles)} on the head. :pleading_face:',
            f'You patted {self.name_format(members_or_roles)} on the head. :pleading_face:'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def poke(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Pokes someone."""
        messages = [
            'You poked your pillow.',
            'You poked yourself.',
            'You poked me.',
            f'You poked {self.name_format(members_or_roles)}.',
            f'You poked {self.name_format(members_or_roles)}.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def punish(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Punishes someone."""
        messages = [
            'You punished your pillow for being naughty I guess.',
            'You punished yourself for being naughty.',
            'I\'m sorry for being so naughty, Master. <:cry2:829114403961438249>',
            f'You punished {self.name_format(members_or_roles)} for being naughty.',
            f'You punished {self.name_format(members_or_roles)} for being very naughty.'
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
            f'You rejected {self.name_format(members_or_roles)}.',
            f'You rejected {self.name_format(members_or_roles)}.'
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
            '<:gunpoint:859930591265161216> <:cry2:829114403961438249>',
            'But M-master... \\*gets shot\\*',
            f'You shot {self.name_format(members_or_roles)}.',
            f'You shot {self.name_format(members_or_roles)}. You\'re a mass murderer now.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['smack'])
    async def slap(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Slaps someone."""
        messages = [
            'You slapped your pillow, since you\'re alone and lonely.',
            'You slapped yourself in the face.',
            'You slapped me. <:cry2:829114403961438249>',
            f'You slapped {self.name_format(members_or_roles)} in the face.',
            f'You slapped {self.name_format(members_or_roles)} in their faces.'
         ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def spank(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Spanks someone."""
        messages = [
            'You didn\'t spank anyone.',
            'You spanked yourself.',
            'You spanked my robot arse. :flushed:',
            f'You spanked {self.name_format(members_or_roles, gen=True)} cute arse.',
            f'You spanked {self.name_format(members_or_roles, gen=True)} cute arses.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def stab(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Stabs someone."""
        messages = [
            'You didn\'t stab anyone.',
            '<:cry2:829114403961438249> :knife:',
            '\\*gets stabbed 23 times\\* Et tu, dominus? \\*dies\\*.',
            f'You brutally stabbed {self.name_format(members_or_roles)}.',
            f'You brutally stabbed {self.name_format(members_or_roles)}.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['suq'])
    async def suck(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Sucks someone off."""
        messages = [
            discord.File(open('bot/assets/images/suck.png', 'rb')),
            'You self-sucked.',
            'You sucked my tiny, robot cock. :flushed:',
            f'You sucked {self.name_format(members_or_roles, gen=True)} monster cock. :flushed:',
            f'You sucked {self.name_format(members_or_roles, gen=True)} monster cocks. :flushed:'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['3some'])
    async def threesome(self, ctx, members_or_roles: commands.Greedy[Union[discord.Member, discord.Role]] = None):
        """Has a threesome with some people."""
        if not members_or_roles:
            await ctx.send('Dude, do you want a hug? <:cry2:829114403961438249>')
        elif len(members_or_roles) == 1:
            await ctx.send(f'You had a threesome with {self.name_format(members_or_roles)} and your pillow.')
        elif len(members_or_roles) == 2:
            await ctx.send(f'You had a threesome with {self.name_format(members_or_roles[:2])}.')
        else:
            await ctx.send(f'You had a threesome with {self.name_format(members_or_roles[:2])} and '
                           f'{self.name_format(members_or_roles[2:])} watched you doing the naughties.')


def setup(bot):
    bot.add_cog(Actions(bot))
