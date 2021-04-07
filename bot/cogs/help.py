import discord
from discord.ext import commands

from ..utils.constants import COLOUR
from ..utils.paginator import EmbedPaginator


# CRED: @Tortoise-Community (https://github.com/Tortoise-Community/Tortoise-BOT/blob/master/bot/cogs/help.py)
class PrettyHelpCommand(commands.MinimalHelpCommand):
    def __init__(self, **options):
        super().__init__()
        self.aliases_heading = options.pop('aliases_heading', 'aliases: ')
        self.paginator = EmbedPaginator(embed_title='Help', page_size=500)

    def add_aliases_formatting(self, aliases):
        self.paginator.add_line(f'({self.aliases_heading}{"; ".join(map(lambda x: f"*`{x}`*", aliases))})')

    def add_command_formatting(self, command):
        if command.description:
            self.paginator.add_line(f'\n{command.description}', empty=True)

        signature = self.get_command_signature(command)
        if command.aliases:
            self.paginator._embed_title = f'*`{signature.strip()}`*'
            self.add_aliases_formatting(command.aliases)
        else:
            self.paginator._embed_title = f'*`{signature.strip()}`*'

        if command.help:
            try:
                self.paginator.add_line(f'\n{command.help}', empty=True)
            except RuntimeError:
                for line in command.help.splitlines():
                    self.paginator.add_line(line)
                self.paginator.add_line()

    def get_opening_note(self):
        return None

    def add_bot_commands_formatting(self, commands_, heading):
        if commands_:
            outputs = [f'`{c.name}` – {c.short_doc}' for c in commands_]
            joined = '\n'.join(outputs)
            self.paginator.add_line(f'\n\n**{heading}**\n')
            self.paginator.add_line(joined)

    async def send_pages(self):
        destination = self.get_destination()
        await self.paginator.start(destination, self.context.author, self.context.bot)


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.help_command = None
        self.original_help_command = bot.help_command
        bot.help_command = PrettyHelpCommand()
        bot.help_command.command_not_found('Sorry. I could\'t find that command.')
        bot.help_command.cog = self

    def cog_unload(self):
        """Revert to default help command if cog is unloaded."""
        self.bot.help_command = self.original_help_command

    @commands.command()
    async def info(self, ctx):
        """Sends information about the bot."""
        msg = (
            'A personal general purpose bot developed for tinkering with creating a bot for Just a chat... servers. '
            f'Use `{ctx.prefix}help [command]` to see its commands.\n\n'
            '[Bot Invite](https://discord.com/api/oauth2/authorize?client_id=764106437701140490&permissions=8'
            '&scope=bot) | [Source Code](https://github.com/jnpoJuwan/Just-a-bot)'
        )

        embed = discord.Embed(title='About Just a bot...', description=msg, colour=COLOUR)
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
