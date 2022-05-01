import discord, os, json,requests
from aiohttp import *
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from requests import head
fObj = open('config.json')
ogdata = json.load(fObj)
deletes = ogdata['delete']
tokenn = ogdata['token']
# Check for token

def tokus(tokn):
  os.system('cls')
  headers = {'Content-Type': 'application/json', 'authorization': tokn}
  url = "https://discordapp.com/api/v6/users/@me/library"
  r = requests.get(url, headers=headers)
  if r.status_code == 200:
      return tokn
  else:
    try:
      print("Invalid or no token provided:\n")
      tokkus = input("Enter your token\n")
      with open('config.json', 'r') as f:
        json_data = json.load(f)
        json_data['token'] = tokkus
        f.close()
      with open('config.json', 'w') as f:
        f.write(json.dumps(json_data, indent = 4, sort_keys=True))
        f.close()
        return tokkus
    except Exception as e:
      print(e)


token = tokus(tokenn)

# Prefix Realtime

async def pre(dortrox, message):
  fObj = open('config.json')
  ogdata = json.load(fObj)
  prefix = ogdata['prefix']
  return prefix

async def HookContent():
  fObj = open('config.json')
  ogdata = json.load(fObj)
  webhook_content = ogdata['webhooks']['webhook_content']
  return webhook_content

async def HookName():
  fObj = open('config.json')
  ogdata = json.load(fObj)
  webhook_name = ogdata['webhooks']['webhook_name']
  return webhook_name

async def Hook():
  fObj = open('config.json')
  ogdata = json.load(fObj)
  webhooks = ogdata['webhooks']['webhook']
  return webhooks

intents = discord.Intents().all()
dortrox = commands.Bot(
    command_prefix=pre,
    self_bot=True,
    help_command=None, 
    intents=intents, 
                     )

Help = ["NUKE COMMANDS", "FUN COMMANDS", "ACTIVITIES COMMANDS", "MAIN COMMANDS"]
Main = [f"purge: Delete messages from a channel  |  purge <amount here>", f"ping: Shows lantency  |  purge", f"webhook: Turn webhooks on & off  |  webhook <true/false>", f"activity: changes activity message  |  activity <message here>", f"nwebhook: Changes webhooks name  |  nwebhook <name here>", f"cwebhook: Changes webhooks content  |  nwebhook <content here>", f"rn : Changes roles name  |  rn <name here>", f"cn: Changes channels name  |  cn <name here>", f"prefix: Changes prefix  |  prefix <New prefix here>" ]
Nuke = [f"nuke: Blow up the server for you  |  nuke" ]
Activites = [f"stream: Change to streaming message and activity  |  stream <messsage here>", f"listen: Change to listening message and activity  |  listen <messsage here>", f"playing: Change to playing message and activity listen <message here>", f"watch: Change to watching message and activity  |  watch <message here>"]
Fun = f"""
```ini
[hastare]\n[otax]\n[danc]\n[langry]\n[hah]\n[owo]\n[lonely]\n[ahh]\n[bbye]\n[hahug]\n[hjump]\n[pat]\n[twerk]\n[nani]\n[love]\n[sesso]\n[jews]\n[cp]\n```
"""

for filename in os.listdir('./runs'):
    if filename.endswith('.py'):
        dortrox.load_extension(f'runs.{filename[:-3]}')

@dortrox.event
async def on_guild_channel_create(channel):
  webhooks = await Hook()
  if webhooks == "True":
    try: 
      webhook = await channel.create_webhook(name=await HookName())
    except Exception as e:
      pass
      
    for i in range(1):
      try:
        await webhook.send(content= await HookContent(), avatar_url='https://media.discordapp.net/attachments/853265428951072789/960967237022416906/nihon.vibe-20220329-0001.jpeg')
      except Exception as e:
        pass
  else:
    pass

@dortrox.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@dortrox.event
async def on_ready():
    os.system("cls")
    await dortrox.change_presence(activity=discord.Streaming(name=ogdata['Activity_name'], url="https://www.twitch.tv/dortrox"))
    print(f"""
                                    
                                   ▄████████  ▄█     ▄████████  ▄█  ███    █▄     ▄████████ 
                                  ███    ███ ███    ███    ███ ███  ███    ███   ███    ███ 
                                  ███    █▀  ███▌   ███    ███ ███▌ ███    ███   ███    █▀  
                                  ███        ███▌  ▄███▄▄▄▄██▀ ███▌ ███    ███   ███        
                                ▀███████████ ███▌ ▀▀███▀▀▀▀▀   ███▌ ███    ███ ▀███████████ 
                                         ███ ███  ▀███████████ ███  ███    ███          ███ 
                                   ▄█    ███ ███    ███    ███ ███  ███    ███    ▄█    ███ 
                                 ▄████████▀  █▀     ███    ███ █▀   ████████▀   ▄████████▀  
                                                    ███    ███                              
                                            Manipulating: {dortrox.user}  
                                                  Prefix: {ogdata['prefix']}                     
    """)



@dortrox.command()
async def help(ctx, content=None):
  try:
    await ctx.message.delete()
  except:
    pass

  h = """>>> **```ini
[S I R I U S SELFBOT]
```**\n""" 
  if content == None:
    h += """```diff
- Ｃａｔｅｇｏｒｙ
```\n\n\n"""
    for i in Help:
      h += f"""***```json
\"{i}\"
```***\n"""
    h += f'''```diff
+ help: To search for a specific category  |  Example : help <category name>
```\n\n'''
  elif content.lower() == "main":
    h += '''```json
"Ｃａｔｅｇｏｒｙ [MAIN]"```\n\n'''
    for i in Main:  
      h += f"""```diff
+ {i}
```\n"""
    
  elif content.lower() == "nuke":
    h += '''```json
"Ｃａｔｅｇｏｒｙ [NUKE]"```\n\n'''
    for i in Nuke:
      h += f"""```diff
+ {i}
```\n"""
  elif content.lower() == "fun":
    h += '''```json
"Ｃａｔｅｇｏｒｙ [FUN]"```\n\n'''
    h += Fun
  elif content.lower() == "activities":
    h += '''```json
"Ｃａｔｅｇｏｒｙ [Activity]"```\n\n'''
    for i in Activites:
      h += f"""```diff
+ {i}
 ```\n"""
  else:
    h += """```diff
- No Result
```"""

  await ctx.send(h, delete_after=deletes)

try:  
  dortrox.run(token, bot=False)
except discord.LoginFailure:
  print("Invalid token provide")