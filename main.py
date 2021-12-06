import colorama
import time
import os
from colorama import Fore
from colorama import Style
from colorama import Back
from colorama import init
init()

print(" ")
print(Fore.RED + "Bienvenue sur HackOrd !")
time.sleep(3)
print(Style.RESET_ALL + " ")
print(Fore.YELLOW + "Veuillez indiquer le nombre de l'outil que vous shouaitez utiliser dans la boite ci dessous.")
print(Style.RESET_ALL + Fore.GREEN + "1) Cloneur de serveur.")
print("2) Selfbot")
print(Style.RESET_ALL + " ")

time.sleep(1)

choice = input("Veuillez indiquer votre choix : ")

print("Chargement...")
time.sleep(0.5)

if choice == "1":
  print(Back.GREEN + "Démarage du cloneur de serveur..." + Style.RESET_ALL)
  os.system('clear')

  time.sleep(0.5)

  os.system('python /src/cloner/main.py')

elif choice == "2":
  print(Back.GREEN + "Démarage du selfbot..." + Style.RESET_ALL)
  os = platform.system()
   if os == "Windows":
      os.system('cls')
   else:
      os.system('clear')

  time.sleep(0.5)

  os.system('python /src/cloner/main.py')

else:
  print(Back.RED + "Aucune option trouvée.")
  print(Style.RESET_ALL + Fore.YELLOW + "Veuillez ressayer.")
  choice = input("Veuillez indiquer votre choix : ")
