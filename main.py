import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="Prefix", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('ログインしました')

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content == "おはよう":
        await message.reply("おはよう！")
        return

    bot.process_commands(message)

@bot.command(name="hello")
async def hello(ctx: commands.Context):
    await ctx.reply("Hello!")

bot.run("Token")