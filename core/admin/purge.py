import typing
import time
from asgiref.sync import sync_to_async
from discord.ext import commands
from discord import NotFound
import discord
from db.models import Example


class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

     @commands.command()
    async def purge(self, ctx, num_messages: int):
        """Clear <n> messages from current channel"""
        channel = ctx.message.channel
        num_messages = num_messages + 1
        info_board = discord.Embed(colour=discord.Colour.dark_red())
        is_admin = await sync_to_async(User.objects.get, thread_sensitive=True)(user_id=ctx.message.author.id,
                                                                                server__server_id=ctx.guild.id)
        try:
            if int(is_admin.server.owner) == int(
                    ctx.message.author.id) or is_admin.is_admin or is_admin.is_mod:
                messages = await channel.history(limit=None).flatten()
                mes_his = await channel.history(limit=num_messages).flatten()

                """Clear <n> messages from current channel"""
                if len(messages) >= num_messages:
                    await channel.purge(limit=num_messages)
                    info_board.add_field(name="Clearing...", value='{} messages was deleted'.format(num_messages))
                    await ctx.send(embed=info_board, delete_after=5)
                elif len(messages) == 0:
                    info_board.add_field(name="Sorry", value='Its nothing to delete :(')
                    await ctx.send(embed=info_board, delete_after=5)
                
                """Clear count messages from current channel"""
                else:
                    await channel.purge(limit=len(messages))
                    info_board.add_field(name="Clearing...", value='{} messages was deleted'.format(len(messages)))
                    await ctx.send(embed=info_board, delete_after=5)


            else:
                info_board = discord.Embed(colour=discord.Colour.dark_gray())
                info_board.add_field(name="DENIAL", value="You don't have permission!")
                await ctx.send(embed=info_board, delete_after=5)
                await ctx.send(ctx.message.author.id)

            await ctx.message.delete()
        except NotFound:
            return print("")

def setup(bot):
    bot.add_cog(Purge(bot))