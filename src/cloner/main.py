mytitle = "TIC Cloner "
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
    os.system("title HackOrd | Cloneur")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}HackOrd | Cloneur de serveurs Discord.
{Style.RESET_ALL}
{Fore.MAGENTA}Cet outil est concidérer comme un selkfbot et est banni par Discord. \n Veuillez ne pas utiliser cet outil sur votre comlpte principal. \n Vous avez été prévenu{Style.RESET_ALL}
        """)

token = input("Veuillez indiquez votre token Discord : \n >")
guild_s = input('Veuillez indiquer l\'ID du serveur que vous shouaitez cloner : \n >')
guild = input('Veuillez indiquer l\'ID du serveur ou sera collé le serveur cloné : \n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}
Serveur cloné avec succes !
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)

    exit_question = input(Fore.BLUE + "Pour retourner a l'accueil, entrez \"1\"." \n > )

    if exit_question == "1":
      print("Retour à l'accueil...")
        if os == "Windows":
            os.system('cls')
            os.system('python main.py')
            
        else:
            os.system('clear')
            os.system('python main.py')
      
      

    client.close()


client.run(token, bot=False)
