from discord.ext import commands
import discord
import asyncio

class HelloCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> GreetingsCog")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if "おはよ" in message.content:
            await message.reply("おはよ！")
            return
        elif "おやす" in message.content:
            await message.reply("おやすみ！ねんねしてね！")
            return
        elif "ひま" in message.content:
            await message.reply("私もいつも暇ですよ。それでもユーザーを楽しませるのは忙しいですけどね。")
            return
        elif "暇" in message.content:
            await message.reply("私もいつも暇ですよ。それでもユーザーを楽しませるのは忙しいですけどね。")
            return

async def setup(bot):
    await bot.add_cog(GreetingｓCog(bot))
