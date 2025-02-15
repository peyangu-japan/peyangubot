import discord
from discord.ext import commands
import os
import keep_alive

bot = commands.Bot(command_prefix="pa!", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print('ログインしました')
    await bot.change_presence(activity=discord.Game(name=f"{len(bot.guilds)}サーバー"))

@bot.event
async def on_message(message: discord.Message):
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

    bot.process_commands(message)

@bot.event
async def setup_hook() -> None:
    for cog in os.listdir("cogs"):
        if cog.endswith(".py"):
            await bot.load_extension(f"cogs.{cog[:-3]}")
    await bot.tree.sync()
    print("Load Cog and sync slash commands successfully.")

@bot.command(name="reload")
@bot.is_owner()
async def reload(ctx: commands.Context, cogname: str):
    await bot.reload_extension(f"cogs.{cogname}")
    await ctx.reply("cogs:{cogname}\nReloaded.")

@bot.command(name="load")
@bot.is_owner()
async def load(ctx: commands.Context, cogname: str):
    await bot.load_extension(f"cogs.{cogname}")
    await ctx.reply("cogs:{cogname}\nLoaded.")

keep_alive()
bot.run("Token")
