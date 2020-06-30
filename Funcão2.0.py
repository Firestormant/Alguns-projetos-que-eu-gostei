from math import sqrt
import colorama
from colorama import Fore, Back, Style
from time import sleep
colorama.init(autoreset=True)


def Funcao(a, b, c):#Definir o Delta
    if a > 0:
        concavidade = "Para Cima"
    else:
        concavidade = "Para Baixo"
    if b >= 0:
        delta = b**2-4*a*c
    else:
        delta = (-b)**2 -4*a*c
    
    if delta < 0:
        delta = 0

    #Definir o X
    raiz = sqrt(delta)
    xl = (-b+raiz)/2
    xll = (-b-raiz)/2

    #Definir o Vértice
    v =(-b/2*a)
    vl = (-b/4*a)

    #oq vai aparecer para o úsuario
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    print("Concavidade "+Fore.RED+f"{concavidade}")
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    sleep(1)
    print(f"Resolvendo a equação "+Fore.RED+ f"{a}x²{b}x{c}"+Style.RESET_ALL)
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    sleep(1)
    print(Fore.RED+f"Delta = {delta}"+Style.RESET_ALL)  
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    sleep(1)
    print(Fore.RED+ f"X'={xl:.2f}\nX''={xll:.2f}"+Style.RESET_ALL)
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    sleep(1)
    print("Vértice = "+Fore.RED+f"{v} e {vl}"+Style.RESET_ALL)
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)


print(Fore.BLUE+"-="*15+Style.RESET_ALL)
a = int(input("Diga seu A:"))
b = int(input("Diga seu B:"))
c = int(input("Diga seu C:"))
Funcao(a, b , c)



