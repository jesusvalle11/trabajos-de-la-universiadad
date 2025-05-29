
import random

def bublesort(m):
    for i in range(5):
        m.append([])
        for j in range(5):
            m[i].append(random.randint(1, 9))
    
    log = len(m)
    for i in range(log):
        for j in range(log - i - 1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
    
    return m


m = []
matrix = bublesort(m)


print("Matriz ordenada:")
for x in matrix:
    print(x)
