from math import sqrt
import colorama
from colorama import Fore, Back, Style
from time import sleep
import Funcões as fp

colorama.init(autoreset=True)


print(Fore.BLUE+"-="*15+Style.RESET_ALL)

a = fp.leia("-Diga seu A: ")
print(Fore.BLUE+"-="*15+Style.RESET_ALL)


b = fp.leia("-Diga seu B: ")
print(Fore.BLUE+"-="*15+Style.RESET_ALL)

print(Fore.BLUE+"-="*15+Style.RESET_ALL)


fp.Funcao(a, b, c)


