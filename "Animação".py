#Animação em cmdkkkkkkkkkkkkkkkkkkkkkkk
def anima():
    from time import sleep
    print("Finalizando", end="")
    for c in range(3):#->Você pode criar um input na hora de chamar a função para adicionar quantos pontos você quiser
        print(".",end="",flush=True)#-> Sem o flush acabou a "animação"
        sleep(1)
anima()
