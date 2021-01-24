import discord
from discord.ext import commands


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'INFO: {__name__} is ready.')

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def cuddle(self, ctx, member: discord.Member = None):
        """Cuddle the member."""
        if member is None:
            await ctx.send('You cuddled your pillow, since you\'re alone and lonely.')
        elif member == ctx.author:
            await ctx.send('You cuddled yourself.')
        elif member == self.bot.user:
            await ctx.send('You cuddled me.')
        else:
            await member.send(f'{ctx.author.name} cuddled you.')
            await ctx.send(f'You cuddled {member.display_name}.')

    @commands.command(aliases=["cri"])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def cry(self, ctx):
        """Cry."""
        file = open('images/cry.jpg', 'rb')
        image = discord.File(file)
        await ctx.send(file=image)

    @commands.command(aliases=['cream', 'jizz'])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def cum(self, ctx, member: discord.Member = None):
        """Cum or cream the member."""
        if member is None or member == ctx.author:
            await ctx.send('Oopsie-doopsie! You cummed all over yourself!')
        elif member == self.bot.user:
            await ctx.send('Y-you want to c-cum inside my tiny robot bussy, master? o///o')
        else:
            await member.send(f'{ctx.author.name} creamed you.')
            await ctx.send(f'You creamed {member.display_name}\'s little bussy. '
                           'You\'re under arrest to horny jail.')

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def fuck(self, ctx, member: discord.Member = None):
        """Fuck the member."""
        if member is None:
            await ctx.send('You fucked your pillow, since you\'re alone and lonely, '
                           'and officially became PD6.')
        elif member == ctx.author:
            await ctx.send('You self-fucked.')
        elif member == self.bot.user:
            await ctx.send('You fucking destroyed my fragile robot bussy.')
        else:
            await member.send(f'{ctx.author.name} fucking destroyed your fragile asshole.')
            await ctx.send(f'You destroyed {member.display_name}\'s fragile asshole. '
                           'You\'re under arrest to horny jail.')

    @commands.command(aliases=['hand_hold', 'hold_hands'])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def hold_hand(self, ctx, member: discord.Member = None):
        """Hold hands with the member."""
        if member is None or member == ctx.author:
            await ctx.send('You held your own hand.')
        elif member == self.bot.user:
            await ctx.send('You held my robot hand.')
        else:
            await member.send(f'{ctx.author.name} held your hand.')
            await ctx.send(f'You committed pre-marital hold handing with {member.display_name}.')

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member = None):
        """Hug the member."""
        if member is None:
            await ctx.send('You hugged your pillow, since you\'re alone and lonely.')
        elif member == ctx.author:
            await ctx.send('You hugged yourself.')
        elif member == self.bot.user:
            await ctx.send('You hugged me. Thanks, I needed one.')
        else:
            await member.send(f'{ctx.author.name} hugged you.')
            await ctx.send(f'You hugged {member.display_name}.')

    @commands.command(aliases=['assassinate', 'murder', 'slaughter'])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def kill(self, ctx, member: discord.Member = None):
        """Kill the member."""
        if member is None:
            await ctx.send('You didn\'t killed anyone.')
        elif member == ctx.author:
            await ctx.send('Hey. You wanna talk about this?')
        elif member == self.bot.user:
            await ctx.send('M-master... *is killed*')
        else:
            await member.send(f'{ctx.author.name} killed you.')
            await ctx.send(f'You have murdered {member.display_name}. You\'re now on the FBI\'s wanted list.')

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member = None):
        """Kiss the member."""
        if member is None:
            await ctx.send('You kissed your pillow, since you\'re lonely.')
        elif member == ctx.author:
            await ctx.send('You kissed yourself.')
        elif member == self.bot.user:
            await ctx.send('You kissed me.')
        else:
            await member.send(f'{ctx.author.name} kissed you.')
            await ctx.send(f'You kissed {member.display_name}.')

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def moan(self, ctx):
        """Moan."""
        file = open('images/moan.png', 'rb')
        image = discord.File(file)
        await ctx.send('And this guy moaned at least this loud.', file=image)

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def poke(self, ctx, member: discord.Member = None):
        """Poke the given member."""
        if member is None or member == ctx.author:
            await ctx.send('You poked yourself.')
        elif member == self.bot.user:
            await ctx.send('You poked me.')
        else:
            await member.send(f'{ctx.author.name} poked you.')
            await ctx.send(f'You poked {member.display_name}.')

    @commands.command()
    async def scream(self, ctx):
        """Scream."""
        file = open('images/scream.jpg', 'rb')
        image = discord.File(file)
        await ctx.send(file=image)

    @commands.command()
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member = None):
        """Slap the member."""
        if member is None or member == ctx.author:
            await ctx.send('You facepalmed.')
        elif member == self.bot.user:
            await ctx.send('You slapped me.')
        else:
            await member.send(f'{ctx.author.name} slapped you.')
            await ctx.send(f'You slapped {member.display_name}.')

    @commands.command(aliases=['suq'])
    @commands.cooldown(3, 60.0, commands.BucketType.user)
    async def suck(self, ctx, member: discord.Member = None):
        """Suck the member."""
        if member is None or member == ctx.author:
            await ctx.send('You self-sucked.')
        elif member == self.bot.user:
            await ctx.send('You sucked my tiny cock.')
        elif member.id == 567488628003962880:  # Dr. IPA#3047
            await member.send(f'{ctx.author.name} suqqed you.')
            await ctx.send(f'You suqqed {member.display_name}. You\'re under arrest to horny jail.')
        else:
            await member.send(f'{ctx.author.name} sucked you.')
            await ctx.send(f'You sucked {member.display_name}. You\'re under arrest to horny jail.')

    @cuddle.error
    @cum.error
    @fuck.error
    @hold_hand.error
    @hug.error
    @kill.error
    @kiss.error
    @poke.error
    @slap.error
    @suck.error
    async def action_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please @mention a member.')


def setup(bot):
    bot.add_cog(Actions(bot))
