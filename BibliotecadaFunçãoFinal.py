def leia(texto):

    import colorama
    from colorama import Fore, Back, Style
    from time import sleep
    colorama.init()
    valido = False
    while not valido:
        entrada = str(input(texto))
        animal()
        if entrada.isalpha() or entrada.strip()=="":
            print(Fore.RED+"ERRO!"+Fore.RESET+f"\"{entrada}\" não é um "+Fore.RED+"número inteiro")
            print(Fore.BLUE+"-="*15+Style.RESET_ALL)
        else:
            valido = True
            return int(entrada)



def Funcao(a=0, b=0, c=0):#Definir o Delta
    from math import sqrt
    import colorama
    from colorama import Fore, Back, Style
    from time import sleep
    colorama.init()
    print("     FUNÇÃO DE 2º GRAU")
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    print(f"Resolvendo a equação "+Fore.RED+ f"{a}x²{b}x{c}")
    sleep(2)
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    print(f"O"+Fore.YELLOW+" Eixo Y "+Fore.RESET+"cortará em " +Fore.RESET+f"{c}")
    sleep(2)
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    


    if a > 0:
        concavidade = "Para Cima"
    else:
        concavidade = "Para Baixo"
    print(f"A Concavidade será "+Fore.RED+f"{concavidade}"+Fore.RESET)
    sleep(2)
    try:
        if b >= 0:
            delta = b**2-4*a*c
        else:
            delta = (-b)**2 -4*a*c

    except:
        print(Fore.RED+"Não há Delta")
        
    else :
        
        print(Fore.BLUE+"-="*15+Style.RESET_ALL) 
        if delta > 0:
            print(Fore.YELLOW+f"Delta = "+Fore.RESET+Fore.RED+f" {delta}"+Style.RESET_ALL)
        else:
            print("Não há" +Fore.YELLOW+ " Delta " +Fore.RESET+ "pois ele foi igual a " +Fore.RED+ f"{delta}")
    sleep(2)
    
      
    
    
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    #Definir o X
    try:
        raiz = sqrt(delta)
        xl = (-b+raiz)/(2*a)
        xll = (-b-raiz)/(2*a)
    except:
        print(Fore.RED+"Não"+Fore.RESET+" há pontos X")
    else:
        print(Fore.YELLOW+f"X' = "+Fore.RESET+Fore.RED+ f"{xl:.2f}"+Fore.RESET+Fore.YELLOW+" X'' = "+Fore.RED+ f"{xll:.2f}")
    sleep(2)

         
    print(Fore.BLUE+"-="*15+Style.RESET_ALL)
    #Definir o Vértice
    v = -b/(2*a)
    vl = -(delta)/(4*a)
    print(Fore.YELLOW+f"Vertices "+Fore.RESET+Fore.RED+f"{v:.2f}"+Fore.RESET+" e "+Fore.RED+f"{vl:.2f}")
    
