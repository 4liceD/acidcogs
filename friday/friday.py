from redbot.core import commands
import datetime
import pytz

class FridayPoster(commands.Cog):
    """Posts a link on Fridays in California"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
