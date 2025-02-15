from discord.ext import commands
import discord
import asyncio

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> AdminCog")

    @commands.command(name="gban")
    @commands.is_owner()
    async def gban(self, ctx: commands.Context, user: discord.User):
        for g in self.bot.guilds:
            await g.ban(user)
            await asyncio.sleep(2)
        await ctx.reply(f"{user.name}をGBANしました。")

async def setup(bot):
    await bot.add_cog(AdminCog(bot))