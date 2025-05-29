import random
def generar_numero():
    return random.randint(1,100)

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


import matplotlib.pyplot as plt
# Datos
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
# Crear gráfico
plt.plot(x, y)
# Etiquetas
plt.title('Gráfico de líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
# Mostrar
plt.show()
