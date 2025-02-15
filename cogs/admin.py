from discord.ext import commands
import discord
import asyncio

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> AdminCog")

    @commands.command(name="guilds_list")
    @commands.is_owner()
    async def guilds_list(self, ctx: commands.Context):
        await ctx.reply(f"サーバーリスト:\n{"\n".join([f"{g.name} - {g.id}" for g in self.bot.guilds])}")

async def setup(bot):
    await bot.add_cog(AdminCog(bot))