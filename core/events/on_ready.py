import discord
from discord.ext import commands

import settings



class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready!")
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))


def setup(bot):
    bot.add_cog(OnReady(bot))
