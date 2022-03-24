import discord
from discord.ext import commands as dortrox

class activities(dortrox.Cog):
    def __init__(self, dortrox):
        self.dortrox = dortrox


    @dortrox.command()
    async def stream(self, ctx,*, content):
        try:
            await ctx.message.edit(content=f'`Streaming: {content}`')
            await self.dortrox.change_presence(activity=discord.Streaming(name=content, url="https://www.twitch.tv/dortrox"))
        except Exception as e:
            print(f"{e}")
            await ctx.message.channel.send(f"""```py\n{e}```""")

    @dortrox.command()
    async def play(self, ctx,*, content):
        try:
            await ctx.message.edit(content=f'`Playing: {content}`')
            await self.dortrox.change_presence(activity=discord.Game(content))
        except Exception as e:
            print(f"{e}")
            await ctx.message.channel.send(f"""```py\n{e}```""")

    @dortrox.command()
    async def watch(self, ctx,*, content):
        try:
            await ctx.message.edit(content=f'`Watching: {content}`')
            await self.dortrox.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= content))
        except Exception as e:
            print(f"{e}")
            await ctx.message.channel.send(f"""```py\n{e}```""")

    @dortrox.command()
    async def listen(self, ctx,*, content):
        try:
            await ctx.message.edit(content=f'`Listening: {content}`')
            await self.dortrox.change_presence(type=discord.Activity.Type.listening, name = content)
        except Exception as e:
            print(f"{e}")
            await ctx.message.channel.send(f"""```py\n{e}```""")

def setup(dortrox):
    dortrox.add_cog(activities(dortrox))