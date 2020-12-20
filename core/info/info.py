import  discord
import random
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(pass_context=True)
    async def info(self,ctx):
        info_board = discord.Embed(
            title="StrawHats Bot",
            description="",
            colour=discord.Colour.red()
        )
        info_board.set_thumbnail(url=ctx.bot.user.avatar_url)
        info_board.set_footer(text="Made by @モンキー･D･ルフィ#8386")
        info_board.set_author(name="StrawHats")
        info_board.add_field(name="Commands", value="Type ?help for commands.", inline=True)

        await ctx.send(embed=info_board)

    @commands.command(pass_context=True)
    async def avatar(self,ctx):
        await ctx.send(ctx.author.avatar_url)

    @commands.command(pass_context=True)
    async def help(self,ctx):
        info_board = discord.Embed(
            title="Command List",

            colour=discord.Colour.blue()
        )
        info_board.set_footer(text="Made by @モンキー･D･ルフィ#8386")
        info_board.set_author(name="StrawHatsBOT")
        info_board.add_field(name="prefix_example_command", value="prefix_example_command", inline=False)
       
        await ctx.send(embed=info_board)

def setup(bot):
    bot.add_cog(info(bot))
