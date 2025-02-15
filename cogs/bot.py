from discord.ext import commands
import discord
import asyncio

class BotCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> BotCog")

    @commands.command(name="invite")
    async def invite_bot(self, ctx: commands.Context):
        await ctx.reply("Botの導入リンク:\nhttps://discord.com/oauth2/authorize?client_id=1283362010985140224。")

async def setup(bot):
    await bot.add_cog(BotCog(bot))
