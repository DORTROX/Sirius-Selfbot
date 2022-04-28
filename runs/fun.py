import discord, time, random, json
from discord.ext import commands as dortrox
fObj = open('config.json',)
ogdata = json.load(fObj)
deletes = ogdata['delete']

ip = ["222.26.23.124","234.199.82.205","26.184.18.105","169.79.216.107","102.161.157.12","38.209.22.224","43.202.231.199","238.190.155.142","26.58.217.135","161.220.253.147","183.214.172.78","154.145.217.213","64.240.232.154","233.185.209.180","198.189.189.239","111.73.1.193","200.163.139.86","13.136.134.192","94.234.235.199","71.223.118.77","67.164.217.134","199.182.193.104","243.72.142.157","81.120.139.63","220.156.204.29","119.32.193.130","91.160.231.82","221.165.30.123","141.241.92.136","117.249.32.159","195.65.81.38","120.110.30.170","127.95.233.240","144.1.87.59","191.238.42.143","245.106.73.181","28.251.102.6","165.135.114.49","153.134.2.232","16.77.128.7","56.195.119.60","55.192.133.37","77.251.68.17","7.66.30.210","52.114.241.222","80.55.130.219","172.223.39.225","39.3.19.108","126.220.137.140","193.228.168.219","225.136.38.57","78.200.157.191","247.91.153.125","46.192.4.222","140.240.138.252","241.183.153.240","232.76.121.7","175.121.70.58","180.237.39.169","245.78.143.124","118.236.21.94","62.25.107.4","246.130.131.91","110.51.4.129","79.203.191.109","86.107.32.91","24.43.154.137","140.133.66.211","4.137.207.111","53.69.40.150","32.91.199.174","136.65.108.131","77.255.5.135","87.201.113.23","3.180.3.224","73.154.50.16","79.48.152.169","243.62.140.225","243.86.237.87","115.112.213.164","133.88.232.145","96.46.13.106","155.40.150.48","152.42.62.76","46.54.31.85","87.179.166.5","149.228.188.65","178.164.198.49","93.85.177.18","80.165.46.190","73.224.136.171","56.189.50.216","95.63.213.156","75.144.252.71","17.222.61.71","30.19.78.21","166.201.211.224","28.58.60.84","193.199.94.79","104.146.37.44"]
passwords = ["imretarded","im retarded","pussylicker","i love cock","sesso","gay","jew","femboy008","JEWS","nigger","Nigga","Solos","Loli slayer","dick","gacharise","ukkisop","dont bend me","Yamate","TinyHomo12","GoodPear347","CoollyWhore288","Ill-informedSmash249","EverCovid-19414","FuturisticLeg179","AboardWanger417","AboardWanger417","OverconfidentTrail327","LovelyPenis498"]

class fun(dortrox.Cog):
    def __init__(self, dortrox):
        self.dortrox = dortrox
        
    @dortrox.command()
    async def danc(self, ctx):
        danc = 'https://images-ext-2.discordapp.net/external/poPP7Gv08VAxIs_v2xQHxcOme1vobWjPZUKg2AaXI4A/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/840794659206987797.gif'
        await ctx.message.edit(content=danc)

    @dortrox.command()
    async def hah(self, ctx):
        hah = 'https://images-ext-1.discordapp.net/external/9bXisJjSpCgJ0h7JqkuZQvwhPAoR1T4GvppqRRvF7Vs/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/767782981073895455.png'
        await ctx.message.edit(content=hah)

    @dortrox.command()
    async def lonely(self, ctx):
        lonely = 'https://images-ext-1.discordapp.net/external/VhJSrbqpdITpmAJj9uTM2ZhkEYv2r7d1Kx6m6uQRyCY/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/859049848413618186.gif'
        await ctx.message.edit(content=lonely)

    @dortrox.command()
    async def ahh(self, ctx):
        ahh = 'https://images-ext-2.discordapp.net/external/Z_w6bKFL5Wxop1bfhTED-ozmy-t3TRwN1CMvg32KkuA/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/755088073884434494.gif'
        await ctx.message.edit(content=ahh)

    @dortrox.command()
    async def bbye(self, ctx):
        bbye = 'https://images-ext-1.discordapp.net/external/FbRZdVStEO91EdORLk2M8ZE4o_qhiWVDloqZUH3noK4/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/712388967902740490.gif'
        await ctx.message.edit(content=bbye)

    @dortrox.command()
    async def twerk(self, ctx):
        twerk = 'https://images-ext-2.discordapp.net/external/t-YyTGVICEGuAptTeteVLVIPorNmDLizca1GWPKfT1w/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/854605974974627881.gif'
        await ctx.message.edit(content=twerk)

    @dortrox.command()
    async def nani(self, ctx):
        nani = 'https://images-ext-1.discordapp.net/external/eUUVCGPbTUmRu_WD7SsTuNUnzDvPZ75sS-7cx5xi5Qg/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/682737787685961832.png'
        nani1 = 'https://images-ext-1.discordapp.net/external/5OVbqNSz2eHVzRecO5cT0T2sb5nrG9OLIR8FLp6qxr8/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/683356400726179876.png'
        nani2 = 'https://images-ext-2.discordapp.net/external/ffQBCA7pQ-NxOKzzMWuLadm8vTtU6blh8LpPz-tHK0M/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/683356144571383810.png'
        await ctx.message.edit(content=nani)
        time.sleep(0.5)
        await ctx.message.edit(content=nani1)
        time.sleep(0.5)
        await ctx.message.edit(content=nani2)

    @dortrox.command()
    async def love(self, ctx):
        try:
                await ctx.message.edit(content="I")
                await ctx.message.edit(content="I love")
                await ctx.message.edit(content="I love you")
                await ctx.message.edit(content="I love your pussy")
                await ctx.message.edit(content="<33")
        except Exception as e:
            print(f"{e}")

    @dortrox.command()
    async def spam(self, ctx, amount=None, * ,message):
        try:
            if amount==None:
                await ctx.message.edit(content="Enter amount")
            else:
                for i in range(int(amount)):
                    await ctx.message.channel.send(message)
        except Exception as e:
            print(e)

    @dortrox.command()
    async def otax(self,ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        guild = ctx.guild
        member = []
        stuff = []
        p = """```OTAXXXED```\n"""
        for gu in guild.members:
            member.append(gu.name)
        for i in range(10):
           name = random.choice(member)
           ipp = random.choice(ip)
           passw = random.choice(passwords)
           stuff.append(f"User: {name}\nIP: {ipp}\nPassword: {passw}")
        for s in stuff:
            p += f"""```{s}```\n"""
        await ctx.message.channel.send(f"{p}", delete_after=deletes)

    @dortrox.command()
    async def sessoo(self, ctx):
        try:
            for i in range(100):
                await ctx.message.edit(content="S")
                time.sleep(2)
                await ctx.message.edit(content="SE")
                time.sleep(2)
                await ctx.message.edit(content="SES")
                time.sleep(2)
                await ctx.message.edit(content="SESS")
                time.sleep(2)
                await ctx.message.edit(content="SESSO")
                time.sleep(2)
        except Exception as e:
            print(f"{e}")
    
    @dortrox.command()
    async def jews(self,ctx):
        await ctx.message.edit(content="🇱 🇴 🇱 🇯 🇪 🇼 🇸")
            
    @dortrox.command()
    async def cp(self,ctx):
        await ctx.message.edit(content="🇨 🇵❓ ❓ ❔")

def setup(dortrox):
    dortrox.add_cog(fun(dortrox))