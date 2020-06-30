def anima():#Animação
    from random import randint
    import colorama
    from time import sleep
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    
    lista = [Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.GREEN, Fore.CYAN, Fore.WHITE, Fore.LIGHTRED_EX]
    nome = ["L", "u", "c","a","s"]
    sobrenome=["W","a","s","i","l","e","w","s","k","i"]
    for c in nome:
        print(lista[randint(0, 7)]+f"{c}", end="", flush=True)
        sleep(0.1)
    print()
    for c in sobrenome:
        print(lista[randint(0, 7)]+f"{c}", end="", flush=True)
        sleep(0.1)
    print()
while True:    
    anima()
