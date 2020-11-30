import json

import discord
import praw
from discord.ext import commands


with open("configs/secrets.json") as cf:
    reddit_api = json.load(cf)["reddit_api"]
    client_id = reddit_api["client_id"]
    client_secret = reddit_api["client_secret"]
    user_agent = reddit_api["user_agent"]


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"INFO: {__name__} is ready.")


def setup(bot):
    bot.add_cog(Reddit(bot))
