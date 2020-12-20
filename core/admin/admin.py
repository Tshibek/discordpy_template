import discord
import random
from discord.ext import commands

from db.models import Example


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    """
    YOU SHOULD GIVE YOUR SELF A ROLE NAMED ADMIN TO USE THIS LIKE THAT OR YOU CAN EDIT THE CODE AND DO IT BY PERMISSIONS.
    """

    give_list = []

    @commands.command(pass_context=True)
    async def giveaway(self, ctx):
        author = ctx.message.author
        role_names = [role.name for role in author.roles]
        if "admin" in role_names:
            members = ctx.guild.members
            for i in members:
                self.give_list.append(i)
            winner = random.choice(self.give_list)
            await ctx.send("{} {}".format("Winner : ", winner))
        else:
            await ctx.send("You don't have permission!")
def setup(bot):
    bot.add_cog(Admin(bot))