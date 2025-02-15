from discord.ext import commands
import discord
import asyncio
import aiohttp
import json

class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> GameCog")

    @commands.command(name="skin")
    async def mc_skin(self, ctx: commands.Context, ユーザーネーム: str):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.mojang.com/users/profiles/minecraft/{ユーザーネーム}') as response:
                    j = json.loads(await response.text())
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f'https://api.minetools.eu/profile/{j["id"]}') as rs:
                            jj = json.loads(await rs.text())
                            await ctx.reply(embed=discord.Embed(title="Minecraftのユーザー情報", description=f"ID: {j["id"]}\nName: {j["name"]}", color=discord.Color.green()).set_thumbnail(url=f"{jj["decoded"]["textures"]["SKIN"]["url"]}").set_image(url=f"https://mc-heads.net/body/{ユーザーネーム}/200"))
        except:
            return await ctx.reply(embed=discord.Embed(title="ユーザー情報の取得に失敗しました。", color=discord.Color.red()))

async def setup(bot):
    await bot.add_cog(GameCog(bot))