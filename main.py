from bot.bot import JustABot
from bot.configs.configs import BOT_TOKEN

bot = JustABot()
print('Loading and starting the bot...')
bot.run(BOT_TOKEN)
