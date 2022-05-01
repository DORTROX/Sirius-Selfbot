import json
from discord.ext import commands as dortrox
global json_data

class main(dortrox.Cog):
    def __init__(self, dortrox):
        self.dortrox = dortrox


    @dortrox.command()
    async def purge(self, ctx, t: int):
        await ctx.message.delete()
        try:
            async for message in ctx.message.channel.history(limit=t).filter(lambda x: x.author == self.dortrox.user).map(lambda x: x):
                await message.delete()
        except:
            pass
        
    @dortrox.command()
    async def ping(self, ctx):
        try:
            await ctx.message.edit(content=f'`{round(self.dortrox.latency * 1000)}ms`')
        except Exception as e:
            print(f"{e}")

    @dortrox.command()
    async def prefix(self, ctx, content):
        global dortrox
        try:
            with open('config.json', 'r') as f:
                json_data = json.load(f)
                json_data['prefix'] = content
                f.close()
            with open('config.json', 'w') as f:
                f.write(json.dumps(json_data, indent = 4, sort_keys=True))
                f.close()
            await ctx.message.edit(content=f"**`Prefix : {content}`**")
        except Exception as e:
            print(e)

    @dortrox.command()
    async def ban(self, ctx):
        try:
            with open('config.json', 'r') as f:
                json_data = json.load(f)
                if json_data['guild']['ban'] == 'True':
                    content = 'False'
                elif json_data['guild']['ban'] == 'False':
                    content = 'True'
                json_data['guild']['ban'] = content
                f.close()
            with open('config.json', 'w') as f:
                f.write(json.dumps(json_data, indent = 4, sort_keys=True))
                f.close()
            await ctx.message.edit(content=f"**`Ban: {content}`**")
        except Exception as e:
            print(e)
            await ctx.message.channel.send(f"""```py\n{e}```""")

    @dortrox.command()
    async def activityN(self,ctx,*, content):
        try:
            with open('config.json', 'r') as f:
                json_data = json.load(f)
                json_data['Activity_name'] = content
                f.close()
            with open('config.json', 'w') as f:
                f.write(json.dumps(json_data, indent = 4, sort_keys=True))
                f.close()
            await ctx.message.edit(content=f"**`On_ready Activity name  : {content}`**")
        except:
            pass

    @dortrox.command()
    async def roleN(self,ctx,*, content):
        try:
            with open('config.json', 'r') as f:
                json_data = json.load(f)
                json_data['guild']['role_json']['name'] = content
                f.close()
            with open('config.json', 'w') as f:
                f.write(json.dumps(json_data, indent = 4, sort_keys=True))
                f.close()
            await ctx.message.edit(content=f"**`Role Name : {content}`**")
        except:
            pass

    @dortrox.command()
    async def channelN(self,ctx,*, content):
        try:
            with open('config.json', 'r') as f:
                json_data = json.load(f)
                json_data['guild']['channel_json']['name'] = content
                f.close()
            with open('config.json', 'w') as f:
                f.write(json.dumps(json_data, indent = 4, sort_keys=True))
                f.close()
            await ctx.message.edit(content=f"**`Channel Name : {content}`**")
        except:
            pass

    @dortrox.command()
    async def guildN(self, ctx,*, content):
        try:
            with open('config.json', 'r') as f:
                json_data = json.load(f)
                json_data['guild']['guildName'] = content
                f.close()
            with open('config.json', 'w') as f:
                f.write(json.dumps(json_data, indent = 4, sort_keys=True))
                f.close()
            await ctx.message.edit(content=f"**`Guild Name : {content}`**")
        except:
            pass


    @dortrox.command()
    async def hooks(self, ctx):
        try:
            with open('config.json', 'r') as f:
                json_data = json.load(f)
                if json_data['webhooks']['webhook'] == 'True':
                    content = 'False'
                elif json_data['webhooks']['webhook'] == 'False':
                    content = 'True'
                json_data['webhooks']['webhook'] = content
                f.close()
            with open('config.json', 'w') as f:
                f.write(json.dumps(json_data, indent = 4, sort_keys=True))
                f.close()
            await ctx.message.edit(content=f"**`Webhooks: {content}`**")
        except Exception as e:
            print(e)
            await ctx.message.channel.send(f"""```py\n{e}```""")

    @dortrox.command()
    async def hooksN(self,ctx,*, content):
        try:
            with open('config.json', 'r') as f:
                json_data = json.load(f)
                json_data['webhooks']['webhook_name'] = content
                f.close()
            with open('config.json', 'w') as f:
                f.write(json.dumps(json_data, indent = 4, sort_keys=True))
                f.close()
            await ctx.message.edit(content=f"**`Webhooks Name : {content}`**")
        except Exception as e:
            print(f'{e}')

    @dortrox.command()
    async def hooksC(self,ctx,*, content):
        try:
            with open('config.json', 'r') as f:
                json_data = json.load(f)
                json_data['webhooks']['webhook_content'] = content
                f.close()
            with open('config.json', 'w') as f:
                f.write(json.dumps(json_data, indent = 4, sort_keys=True))
                f.close()
            await ctx.message.edit(content=f"**`Webhook Content : {content}`**")
        except:
            pass
            

def setup(dortrox):
    dortrox.add_cog(main(dortrox))