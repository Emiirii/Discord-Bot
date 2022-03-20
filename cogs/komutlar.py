import discord 
from discord.ext import commands

from main import Bot

class Komutlar(commands.Cog):
    def __init__(self, Bot):
        self.bot = Bot


    @commands.command()
    async def merhaba(self, ctx):
        await ctx.send("Merhaba")


def setup(bot):
    bot.add_cog(Komutlar(bot))
