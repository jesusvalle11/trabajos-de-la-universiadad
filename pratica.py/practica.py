import random
m =[]
suma =0
sumapar = 0
verpar = []
verimp =[]
sumaimpar = 0
mayor = 0
menor = 10
contmy = 0
contmn = 0
contar_impar= 0
contar_par = 0

for i in range(5):
  m.append([])
  for j in range(5):
    m[i].append(random.randint(1,9))
    print(m[i][j],end=" ")
  print("")

for i in range(5):
  for j in range(5):
    suma = suma+m[i][j]
    if m[i][j] > mayor:
      mayor = m[i][j]
    if m[i][j] < menor:
      menor = m[i][j]
    if m[i][j] % 2 == 0:
      contar_par = contar_par + 1
      sumapar=sumapar+m[i][j]
      verpar.append(m[i][j])
    else:
      contar_impar = contar_impar + 1
      sumaimpar=sumaimpar+m[i][j]
      verimp.append(m[i][j])

for i in range(5):
  for j in range(5):
    if m[i][j] ==mayor:
      contmy = contmy+1 

for i in range(5):
  for j in range(5):
    if m[i][j] == menor:
       contmn = contmn+1 
              
  
suma_ultima= sum(m[-1])
prom = suma/(len(m) * len(m[0]))
print("el promedio de la  matriz:",prom)
print("la suma de los elementos es:",suma)
print("la suma de los elementos pares es:",sumapar)
print("la suma de los elementos impares es:",sumaimpar)
print("numeros pares:", verpar)
print("numeros impares:",verimp)
print("pomedio de los numeros pares:",sumapar/contar_par)
print("pomedio de los numeros impares:",sumaimpar/contar_impar)
print("numero mayor es:",mayor,"y se repite",contmy,"veces")
print("numero menor es:",menor,"y se repite",contmn,"veces")
print("la suma de los elementos de la ultima fila es:",suma_ultima)

filas = len(m)
columnas = len(m[0])
if filas == columnas:
    print("La matriz es cuadrada.")
    diagonal_principal = []
    for i in range(filas):
        diagonal_principal.append(m[i][i])
        print(m[i][i], end=" ")
    print("\nDiagonal principal:", diagonal_principal)
else:
    print("La matriz no tiene diagonal principal, no es cuadrada.")