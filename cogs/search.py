from discord.ext import commands
import discord
import asyncio

class SearchCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> SearchCog")

    @commands.command(name="user")
    async def user_search(self, ctx:commands.Context, user: discord.User):
        embed = discord.Embed(title=user.display_name, description=f"作成日: {user.created_at}\nID: {user.id}\n名前: {user.name}", color=discord.Color.green())
        if user.avatar:
            embed.set_thumbnail(url=user.avatar.url)
        await ctx.reply(embed=embed)

    @commands.command(name="avatar")
    async def avatar_search(self, ctx:commands.Context, user: discord.User):
        embed = discord.Embed(title=f"{user.display_name}さんのアバター", color=discord.Color.green())
        if user.avatar:
            embed.set_thumbnail(url=user.avatar.url)
        else:
            embed.set_thumbnail(url=user.default_avatar.url)
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(SearchCog(bot))