m = []

for i in range(6):
    m.append([])
    for j in range(6):
        if (i==j):
            m[i].append(1)
        elif i + j == 5:
            m[i].append(1)
        else:    
            m[i].append(0)    
        print(m[i][j],end=" ")
    print(" ")    
print("\n")

for i in range(6):
    for j in range(6):
     print(f"({i},{j})",end=" ")
    print(" ")          