import random
import typing as t

import discord
from discord.ext import commands


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_names(self, member_or_roles, genitive=False):
        output = []

        for obj in member_or_roles:
            if not genitive:
                if isinstance(obj, discord.Member):
                    output.append(obj.display_name)
                else:
                    output.append(obj.name)
            else:
                if isinstance(obj, discord.Member):
                    output.append((obj.display_name + '\'' if obj.display_name.lower().endswith('s')
                                   else obj.display_name + '\'s'))
                else:
                    output.append((obj.name + '\'' if obj.name.lower().endswith('s') else obj.name + '\'s'))

        return output

    def format_list(self, members_or_roles=None, genitive=False):
        if not members_or_roles:
            return

        members_or_roles = self.get_names(members_or_roles, genitive)

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
                await member.send(messages[4])

    @commands.command()
    async def bonk(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Bonks someone."""
        messages = [
            'You didn\'t bonk anyone.',
            'You bonked yourself to horny jail.',
            'You bonked me to horny jail.',
            f'You bonked {self.format_list(members_or_roles)} to horny jail.',
            f'{ctx.author.name} bonk you to horny jail.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def cuddle(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Cuddles someone."""
        messages = [
            'You cuddled your pillow, since you\'re alone and lonely.',
            'You cuddled yourself.',
            'You cuddled me.',
            f'You cuddled {self.format_list(members_or_roles)}.',
            f'{ctx.author.name} cuddled you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=["cri"])
    async def cry(self, ctx):
        """Cries."""
        image = discord.File(open('bot/assets/images/cry.jpg', 'rb'))
        await ctx.send('<:cat_cry:814925690528333885>', file=image)

    @commands.command(aliases=['ejaculate', 'cream', 'jizz', 'nut', 'sperm', 'splooge'])
    async def cum(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Cums or creams someone."""
        messages = [
            'Oopsie-doopsie! You cummed all over yourself!',
            'You creamed yourself.',
            'You want to c-cum inside my tiny robot bussy, master? o//w//o',
            f'You creamed {self.format_list(members_or_roles)}\'s little þussy. You\'re under arrest to horny jail.',
            f'{ctx.author.name} creamed you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['dnace'])
    async def dance(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Dance with someone."""
        messages = [
            'You *dnaced*.',
            'You danced with yourself.',
            'You danced with me.',
            f'You danced with {self.format_list(members_or_roles)}.',
            f'{ctx.author.name} danced with you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def frost(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Frosts someone."""
        messages = [
            discord.File(open('bot/assets/images/frost.png', 'rb')),
            'You frosted yourself like a birthday cake.',
            'You frosted me like a birthday cake.',
            f'You frosted {self.format_list(members_or_roles, genitive=True)} like a birthday cake.',
            f'{ctx.author.name} frosted you like a birthday cake.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['fuq', 'fwk', 'destroy', 'sex'])
    async def fuck(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Fucks someone."""
        messages = [
            'You fucked your pillow, since you\'re alone and lonely, and officially became PD6.',
            'You self-fucked.',
            'You fucked my tiny robot þussy. 😳 👉👈',
            f'You fucked {self.format_list(members_or_roles, genitive=True)} þussy. You\'re under arrest to horny jail.',
            f'{ctx.author.name} fucked your þussy.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['hand_hold', 'hold_hands'])
    async def hold_hand(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Holds hands with someone."""
        messages = [
            'You didn\'t hold anybody\'s hand.',
            'You held your own hand, since you\'re alone and lonely.',
            'You held my robot hand.',
            f'You committed pre-marital hand holding with {self.format_list(members_or_roles)}.',
            f'{ctx.author.name} fucking destroyed your fragile asshole.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def hug(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Hugs someone."""
        messages = [
            'You hugged your pillow, since you\'re alone and lonely.',
            'You hugged yourself.',
            'You hugged me. I appreciate it. 🥺',
            f'You hugged {self.format_list(members_or_roles)}.',
            f'{ctx.author.name} hugged you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['assassinate', 'murder', 'slaughter'])
    async def kill(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Brutally kills someone."""
        messages = [
            'You didn\'t killed anyone.',
            '<:cat_cry:814925690528333885> <:hug:810945431005560843>',
            'But m-master... \\*is brutally killed\\*',
            f'You have murdered {self.format_list(members_or_roles)}. You\'re now on MAGNVS\' wanted list.',
            f'{ctx.author.name} killed you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def kiss(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Kisses someone."""
        messages = [
            'You kissed your pillow, since you\'re alone and lonely.',
            'You kissed yourself.',
            'You kissed me, master. 🥺',
            f'You kissed {self.format_list(members_or_roles)}. 😳 👉👈',
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
    async def pat(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Pats someone on the head."""
        messages = [
            'You patted your pillow, since you\'re alone and lonely.',
            'You patted yourself.',
            'You patted me. 🥺',
            f'You patted {self.format_list(members_or_roles)} on the head.',
            f'{ctx.author.name} patted you on the head.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def poke(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Pokes someone."""
        messages = [
            'You poked your pillow, since you\'re alone and lonely.',
            'You poked yourself.',
            'You poked me.',
            f'You poked {self.format_list(members_or_roles)}.',
            f'{ctx.author.name} poked you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def punish(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Punishes someone."""
        messages = [
            'You didn\'t punish anyone.',
            'You punished yourself for being naughty.',
            'You punished me for being naughty.',
            f'You punished {self.format_list(members_or_roles)} for being naughty.',
            f'{ctx.author.name} punished you for being naughty.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def reject(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Rejects someone."""
        messages = [
            'You didn\'t reject anyone.',
            'You rejected yourself. <:noooooooo:809935851052072980>',
            'You rejected me. <:noooooooo:809935851052072980>',
            f'You rejected {self.format_list(members_or_roles)}.',
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
    async def shoot(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Shoots someone."""
        messages = [
            'You didn\'t shoot anyone.',
            '<:cat_cry:814925690528333885> <:hug:810945431005560843>',
            '\\*gets shot\\*.',
            f'You shot {self.format_list(members_or_roles)}.',
            f'{ctx.author.name} shot you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def shy_hug(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Shyly hugs someone."""
        messages = [
            'You hugged your pillow, since you\'re alone and lonely.',
            'You hugged yourself.',
            'You hugged me. I appreciate it. 🥺',
            f'You hugged {self.format_list(members_or_roles)}. 😳 👉👈',
            f'{ctx.author.name} hugged you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def slap(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Slaps someone's face or their thicc, juicy arse."""
        choices = [
            ('You facepalmed.',
             'You slapped me.',
             f'You slapped {self.format_list(members_or_roles)}.',
             f'{ctx.author.name} slapped you.'),

            ('You slapped your own thicc arse',
             'You slapped my arse.',
             f'You slapped {self.format_list(members_or_roles)}\'s thicc arse.',
             f'{ctx.author.name} slapped your thicc arse.')
        ]
        messages = random.choice(choices)

        await self.interact(ctx, messages, members_or_roles)

    @commands.command()
    async def stab(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Stabs someone."""
        messages = [
            'You didn\'t stab anyone.',
            '<:cat_cry:814925690528333885> <:hug:810945431005560843>',
            '\\*gets stabbed 23 times\\* Et tu, dominus? \\*dies\\*.',
            f'You brutally stabbed {self.format_list(members_or_roles)}.',
            f'{ctx.author.name} stabbed your heart.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @commands.command(aliases=['suq'])
    async def suck(self, ctx, members_or_roles: commands.Greedy[t.Union[discord.Member, discord.Role]] = None):
        """Sucks someone off."""
        messages = [
            discord.File(open('bot/assets/images/suck.png', 'rb')),
            'You self-sucked.',
            'You sucked my tiny cock.',
            f'You sucked {self.format_list(members_or_roles)}. You\'re under arrest to horny jail.',
            f'{ctx.author.name} sucked you.'
        ]

        await self.interact(ctx, messages, members_or_roles)

    @bonk.error
    @cuddle.error
    @cum.error
    @dance.error
    @fuck.error
    @hold_hand.error
    @hug.error
    @kill.error
    @kiss.error
    @poke.error
    @punish.error
    @reject.error
    @shoot.error
    @slap.error
    @stab.error
    @suck.error
    async def member_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please @mention a member.')


def setup(bot):
    bot.add_cog(Actions(bot))
