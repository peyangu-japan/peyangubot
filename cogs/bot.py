from discord.ext import commands
import discord
import asyncio

class BotCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> BotCog")

    @commands.command(name="invite")
    async def invite_bot(self, ctx: commands.Context):
        await ctx.reply("Botの導入リンク:\nここに導入リンクを置く。")

async def setup(bot):
    await bot.add_cog(BotCog(bot))