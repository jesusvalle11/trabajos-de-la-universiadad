
import random

m = []
mb = []
mc = []
r = []
suma = 0
x = []

for i in range(6):
    m.append([])
    mb.append([])
    for j in range(6):
        m[i].append(random.randint(1,9))
        mb[i].append(random.randint(1,9))
        print(m[i][j],end=" ")
    print("")
print("")        

print("matriz b \n")
for i in range(6):
    for j in range(6):
        print(mb[i][j],end=" ")
    print("")
print("")        

print("matriz A + B \n")
for i in range(6):
    mc.append([])
    for j in range(6):
        mc[i].append(m[i][j] + mb[i][j])
        print(mc[i][j],end=" ")
    print("")
print("")        

print("matriz A - B \n")
r = []
for i in range(6):
    r.append([])
    for j in range(6):
        r[i].append(m[i][j] - mb[i][j])
        print(r[i][j],end=" ")
    print("")
print("")        


x = []
for k in range(6):
    x.append([])
    for i in range(6):
        suma = 0
        for j in range(6):
            suma+= m[i][k] * mb[k][j]
        x[k].append(suma)
        
print("matriz A * B \n")

for i in range(6):
    for j in range(6):
        print(x[i][j],end=" ")
    print("")
    
        
        
            
        

