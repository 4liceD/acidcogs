"""MIT License

Copyright (c) 2025-present 4liced

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
from redbot.core import commands
import datetime
import pytz
import asyncio

class FridayPoster(commands.Cog):
    """Posts a link on Fridays in California"""

    def __init__(self, bot):
        self.bot = bot
        self.post_channel = {}
        self.post_toggle = {}
        self.link = "https://www.youtube.com/watch?v=9WaYCdQ8FOQ"

    @commands.command()
    @commands.has_permissions(manage_guild=true)
    async def setfridaychannel(self, ctx, channel: Commands.ChannelConverter):
        """Set the channel to post the link in"""
        self.post_channel[ctx.guild.id] = channel.id
        await ctx.send(f"Channel set to {channel.mention}")

    @commands.command()
    @commands.has_permissions(managa_guild=true)
    async def togglefridaypost(self, ctx):
        """Toggle whether to post the link on Fridays"""
        if ctx.guild.id not in self.post_toggle:
            self.post_toggle[ctx.guild.id] = False
        self.post_toggle[ctx.guild.id] = not self.post_toggle[ctx.guild.id]
        await ctx.send(f"Friday post toggle set to {self.post_toggle[ctx.guild.id]}")

    @commands.command()
    @commands.has_permissions(manage_guild=true)
    async def testfridaymessage(self, ctx):
        """Test the Friday message"""
        if ctx.guild.id in self.post_channel:
            channel = ctx.guild.get_channel(self.post_channel[ctx.guild.id])
            if channel and self.post_toggle[ctx.guild.id]:
                await channel.send(f"It's Friday in California! Click here to get started: {self.link}")
            else:
                ctx.send("Please set the Friday channel first.")

    @commands.cog_listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.check_friday())

    async def check_friday(self):
        await self.bot.waut_until_ready()
        while not self.bot.is_closed():
            now = datetime.datetime.now(pytz.timezone('US/Pacific'))
            if now.weekday() == 4 and now.hour == 0 and now.minute == 1: # 4 is Friday in Python datetime
                if guild in self.bot.guilds:
                    if guild.id in self.post_channel and guild.id in self.post_toggle and self.post_toggle[guild.id]:
                        channel = guild.get_channel(self.post_channel[guild.ic])
                        if channel:
                            await channel.send(f"It's Friday in California! Ckick here to get started: {self.link}")
                            await asyncio.sleep(60)