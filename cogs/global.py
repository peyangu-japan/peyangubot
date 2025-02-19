from discord.ext import commands
import discord
import aiosqlite
import asyncio

class GlobalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"init -> GlobalCog")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        if message.author.bot:
            return

        if not message.content:
            return

        if "discord.com" in message.content:
            return
        if "discord.gg" in message.content:
            return
        if "discord.gg" in message.content:
            return
        if "x.gd" in message.content:
            return
        if "<sound:" in message.content:
            return

        conn = await aiosqlite.connect("database.db")
        cursor = await conn.cursor()

        try:

            await cursor.execute("SELECT * FROM global_chat WHERE guild_id = ? AND channel_id = ?", (message.guild.id, message.channel.id))
            result = await cursor.fetchone()

            if result:
                for row in cursor.execute("SELECT * FROM global_chat"):
                    guild_id = row[0]
                    channel_id = row[1]
                    channel = self.bot.get_channel(channel_id)

                    webhooks = await channel.webhooks()
                    webhook = next((w for w in webhooks if w.name == "GlobalChatWebhook"), None)
                    if webhook is None:
                        webhook = await channel.create_webhook(name="GlobalChatWebhook")

                    await webhook.send(
                        content=f"{message.content}",
                        username=message.author.name,
                        avatar_url=message.author.avatar.url if message.author.avatar else None
                    )

                    await asyncio.sleep(2)
            await cursor.close()
            await conn.close()
        except:
            return
        

    @commands.group(name="global")
    async def global_(self, ctx: commands.Context):
        return
    
    @global_.command(name="activate")
    async def global_activate(self, ctx: commands.Context):
        conn = await aiosqlite.connect("database.db")
        cursor = await conn.cursor()
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS global_chat (
                guild_id INTEGER,
                channel_id INTEGER
            )
        """)
        await cursor.execute("INSERT INTO global_chat (guild_id, channel_id) VALUES (?, ?)", (ctx.guild.id, ctx.channel.id))
        await conn.commit()
        await cursor.close()
        await conn.close()
        await ctx.reply("グローバルチャットを有効化しました。")
        return

    @global_.command(name="deactivate")
    async def global_deactivate(self, ctx: commands.Context):
        conn = await aiosqlite.connect("database.db")
        cursor = await conn.cursor()
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS global_chat (
                guild_id INTEGER,
                channel_id INTEGER
            )
        """)
        await cursor.execute("DELETE FROM global_chat WHERE guild_id = ? AND channel_id = ?", (ctx.guild.id, ctx.channel.id))
        await conn.commit()
        await cursor.close()
        await conn.close()
        await ctx.reply("グローバルチャットを無効化しました。")
        return

async def setup(bot):
    await bot.add_cog(GlobalCog(bot))