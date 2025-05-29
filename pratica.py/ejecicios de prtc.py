import random
m = []

for i in range(3):
    m.append([])
    for j in range(3):
        m[i].append(random.randint(1,9))
        print(m[i][j],end=" ")
    print(" ")
   




import random
m = []

for i in range(5):
    m.append([])
    for j in range(5):
        m[i].append(random.randint(0,10))
        print(m[i][j],end=" ")
    print(" ")
    
    
    
import random

matriz = []
suma = 0


for i in range(4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(random.randint(1, 9))
        print(matriz[i][j], end=' ')
    print("")


fila = int(input("Ingrese una fila válida (0-3): "))
           
while fila < 0 or fila > 3:
    fila = int(input("Fila incorrecta. Ingrese una fila válida (0-3): "))

print(f"Valores de la fila {fila}: ", end='')
for col in range(4):
    suma += matriz[fila][col]
    print(matriz[fila][col], end=' ')
print(f"\nLa suma de la fila {fila} es {suma}")

suma = 0

col = int(input("Ingrese una columna válida (0-3): "))
while col < 0 or col > 3:
    col = int(input("Columna incorrecta. Ingrese una columna válida (0-3): "))

print(f"Valores de la columna {col}: ", end='')
for fila in range(4):
    suma += matriz[fila][col]
    print(matriz[fila][col], end=' ')
print(f"\nLa suma de la columna {col} es {suma}")

suma = 0


print("Valores de la diagonal principal: ")
for i in range(4):
    suma += matriz[i][i]
    print(matriz[i][i], end=' ')
print(f"\nLa suma de la diagonal principal es {suma}")

suma = 0


print("Valores de la diagonal inversa: ", end='')
for i in range(4):
    suma += matriz[i][3 - i]
    print(matriz[i][3 - i], end=' ')
print(f"\nLa suma de la diagonal inversa es {suma}")
    
    