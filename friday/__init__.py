from .friday import FridayPoster


async def setup(bot):
    await bot.add_cog(MyCog(bot))
