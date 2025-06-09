import random

def generar_numero():
    return random.randint(1, 10)  # genera un número aleatorio entre 1 y 10

def jugar():
    intentos=3
    num_aleatorio=generar_numero()
    print(num_aleatorio)
    x=True

    while intentos>0:
        num=int(input("Ingresa un número"))
        
        if num==num_aleatorio:
            print("Adivinaste!")
            x=False
            break
        else:
            print("Sigue intentando")
        intentos-=1
        if intentos==0 and x==True:
            print("No te quedan más intentos")
jugar()