from discord.ext import commands
import discord
import asyncio

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> AdminCog")

async def setup(bot):
    await bot.add_cog(AdminCog(bot))