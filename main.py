import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="pa!", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print('ログインしました')
    await bot.change_presence(activity=discord.Game(name=f"{len(bot.guilds)}サーバー"))

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content == "おはよう":
        await message.reply("おはよ！")
        return
    elif message.content == "おやすみ":
        await message.reply("おやすみ！ねんねしてね！")
        return

    bot.process_commands(message)

@bot.event
async def setup_hook() -> None:
    for cog in os.listdir("cogs"):
        if cog.endswith(".py"):
            await bot.load_extension(f"cogs.{cog[:-3]}")
    await bot.tree.sync()
    print("Cogの読み込みとスラッシュコマンドの同期に成功しました。")

@bot.command(name="reload")
@bot.is_owner()
async def reload(ctx: commands.Context, cogname: str):
    await bot.reload_extension(f"cogs.{cogname}")
    await ctx.reply("再読み込みしました。")

bot.run("Token")