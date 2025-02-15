from discord.ext import commands
import discord

class ErrorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> ErrorCog")

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = None
            return a
        elif isinstance(error, commands.NotOwner):
            a = None
            return a

async def setup(bot):
    await bot.add_cog(ErrorCog(bot))