from discord.ext import commands
import discord
import aiosqlite
import asyncio
import sys

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
        if "is.gd" in message.content:
            return
        if "v.gd" in message.content:
            return
        if "tinyurl.com" in message.content:
            return
        if "rb.gy" in message.content:
            return
        if "<sound:" in message.content:
            return

        async with aiosqlite.connect("database.db") as conn:  # データベース接続をコンテキストマネージャーで管理
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT * FROM global_chat WHERE guild_id = ? AND channel_id = ?", (message.guild.id, message.channel.id))
                result = await cursor.fetchone()

                if result:
                    await cursor.execute("SELECT * FROM global_chat")
                    rows = await cursor.fetchall()

                    for row in rows:
                        guild_id = row[0]
                        channel_id = row[1]
                        channel = self.bot.get_channel(channel_id)

                        if channel != message.channel:
                            try:
                                webhooks = await channel.webhooks()
                                webhook = next((w for w in webhooks if w.name == "GlobalChatWebhook"), None)
                                if webhook is None:
                                    webhook = await channel.create_webhook(name="GlobalChatWebhook")

                                if message.reference:
                                    msg = await message.channel.fetch_message(message.reference.message_id)
                                    await webhook.send(
                                        content=f"{message.content}\n-# mID:{message.id}",
                                        username=f"{message.author.display_name}(@{message.author.name} - {message.author.id}) | {message.guild.name}",
                                        avatar_url=message.author.avatar.url if message.author.avatar else None,
                                        embed=discord.Embed(title="返信", description=f"{msg.content}")
                                    )
                                    continue

                                await webhook.send(
                                    content=f"{message.content}\n-# mID:{message.id}",
                                    username=f"{message.author.display_name}(@{message.author.name} - {message.author.id}) | {message.guild.name}",
                                    avatar_url=message.author.avatar.url if message.author.avatar else None
                                )
                            except Exception as e:
                                print(f"Webhook error: {e}")

                            await asyncio.sleep(0.5)
        

    @commands.group(name="global")
    async def global_(self, ctx: commands.Context):
        return
    
    @global_.command(name="setup")
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
        await ctx.reply("グローバルチャットをオンにしました。")
        return

    @global_.command(name="disable")
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
        await ctx.reply("グローバルチャットをオフにしました。")
        return

async def setup(bot):
    await bot.add_cog(GlobalCog(bot))
