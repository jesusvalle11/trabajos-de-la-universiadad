
import math

def imprimir_menu():
    print("calculadora")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    print("5.potenciacion")
    print("6.raiz cuadrada")
    print("7.salir")

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        print("no se puede dividir entre cero")

def potenciacion(a,b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        print("no se puede calcular la raiz de un numero negativo.")

def calculadora():
    while True:  # agregar bucle para repetir menú
        imprimir_menu()
        try:
            opcion = int(input("ingrese una opcion: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 7:  # opción para salir
            print("Saliendo de la calculadora...")
            break

        if opcion in [1,2,3,4,5]:
            try:
                a = float(input("ingrese el primer numero:"))
                b = float(input("ingrese el segundo numero: "))
            except ValueError:
                print("Entrada inválida. Por favor ingrese números válidos.")
                continue

        if opcion == 1:
            resultado = suma(a,b)
        elif opcion == 2:
            resultado = resta(a,b)
        elif opcion == 3:
            resultado = multiplicacion(a,b)
        elif opcion == 4:
            resultado = division(a,b)
        elif opcion == 5:
            resultado = potenciacion(a,b)
        elif opcion == 6:
            try:
                a = float(input("ingrese el numero de la raiz: "))
                resultado = raiz_cuadrada(a)
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número válido.")
                continue
        else:
            print("opcion invalidad")
            continue  # vuelve al menú principal

        if resultado is not None:
            print("El resultado es:", resultado)

calculadora()
