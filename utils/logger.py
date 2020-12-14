import logging

logger = logging.getLogger("bot")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="a")
handler.setFormatter(logging.Formatter("%(name)s %(levelname)s %(asctime)s: %(message)s"))
logger.addHandler(handler)
