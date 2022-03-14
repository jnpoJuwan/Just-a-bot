from bot.bot import JustABot
from bot.configs.configs import BOT_TOKEN, TEST_BOT_TOKEN, TEST

bot = JustABot()
print('Loading and starting the bot...')

if TEST:
    bot.run(TEST_BOT_TOKEN)
else:
    bot.run(BOT_TOKEN)
