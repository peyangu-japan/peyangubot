import discord
from discord.ext import commands
import os
import aiosqlite # pip install aiosqlite

class PeyanguBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix="pa!",
            help_command=None,
            intents=discord.Intents.all(),
        )
        print("InitDone")

bot = PeyanguBot()

@bot.event
async def on_ready():
    print('Logged in.')
    await bot.change_presence(activity=discord.Game(name=f"{len(bot.guilds)}サーバー"))

@bot.event
async def setup_hook() -> None:
    for cog in os.listdir("cogs"):
        if cog.endswith(".py"):
            await bot.load_extension(f"cogs.{cog[:-3]}")
    await bot.tree.sync()
    print("Load Cog and sync slash commands successfully.")

@bot.command(name="reload")
@commands.is_owner()
async def reload(ctx: commands.Context, cogname: str):
    await bot.reload_extension(f"cogs.{cogname}")
    await ctx.reply("cogs:{cogname}\nReloaded.")

@bot.command(name="load")
@commands.is_owner()
async def load(ctx: commands.Context, cogname: str):
    await bot.load_extension(f"cogs.{cogname}")
    await ctx.reply("cogs:{cogname}\nLoaded.")

bot.run("Token")
