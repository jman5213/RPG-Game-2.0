#import test
from colorama import Style, Fore
import cursor

print(  f"""{Style.BRIGHT}{Fore.LIGHTBLUE_EX}
    ▄▀█ █▀█ █▀█ █▀█ █ █ █ █▀▀ ▄▀█ █   █
    █▀█ █▀▄ █▀▄ █▄█ ▀▄▀▄▀ █▀  █▀█ █▄▄ █▄▄{Fore.WHITE}""")

print("""
  ▀▀█ █▀█ █▀█ █▀▄ ▄▀█ █▀▄
  ▄▄▀ █▄█ █▀▄ █▄▀ █▀█ █ █""")


bold = Style.BRIGHT
dim = Style.DIM
reset = Style.RESET_ALL

blue = Fore.BLUE
lightblue = Fore.LIGHTBLUE_EX
lightmagenta = Fore.LIGHTMAGENTA_EX
magenta = Fore.MAGENTA
cyan = Fore.CYAN
lightcyan = Fore.LIGHTCYAN_EX
white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
lightyellow = Fore.LIGHTYELLOW_EX

cursor.hide()