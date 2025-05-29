import random
ma = []
mb = []
mc = []
e = []
c =[]
suma = 0
print("matriz A\n")

for i in range(5):
  ma.append([])
  mb.append([])

  for j in range(5):
    ma[i].append(random.randint(1,10))
    mb[i].append(random.randint(1,10))
    print(ma[i][j],end=" ")
  print(" ")
print("")

print("matriz B\n")
for i in range(5):
  for j in range(5):
    print(mb[i][j],end=" ")
  print("")
print("")

print("matriz A+B\n")
for i in range(5):
  mc.append([])
  for j in range(5):
    mc[i].append(ma[i][j]+ mb[i][j])
    print(mc[i][j],end=" ")
  print("")
print("")

print("matriz A-B\n")
c = []
for i in range(5):
    c.append([])
    for j in range(5):
        c[i].append(ma[i][j] - mb[i][j])
        print(c[i][j], end=" ")
    print("")
print("")

print("matriz e (A * B)\n")
e = []
for k in range(5):
    e.append([])
    for i in range(5):
        suma = 0
        for j in range(5):
            suma += ma[i][k] * mb[k][j]
        e[k].append(suma)


print("multiplicar la matriz A*B")
for i in range(5):
    for j in range(5):
        print(e[i][j], end=" ")
    print(" ")