from discord.ext import commands
import discord

class GlobalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> GlobalCog")


async def setup(bot):
    await bot.add_cog(GlobalCog(bot))