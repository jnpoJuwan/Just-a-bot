from bot import JustABot
from configs.configs import BOT_TOKEN, COGS

bot = JustABot()
for module in COGS:
	bot.load_extension(module)
bot.run(BOT_TOKEN)
