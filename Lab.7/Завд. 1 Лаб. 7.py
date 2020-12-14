R = int(input("Кількість рядків R = "))
E = int(input("Кількість елементів E = "))

import random
a = [[random.randint(-100,100) for j in range(E)] for i in range(R)]

b = []

for row in a:
    row_str=['{0:5d}'.format(el) for el in row]
    b.append(row_str)

b = [''.join(['{0:5d}'.format(el) for el in row]) for row in a]
print(*b,sep='\n')

s = 0
for i in range(1,R,2):
    for j in range(1,E,2):
        if a[i][j]<0:
            s*=a[i][j]
print("Cума відємних елементів матриці з обома непарними індексами= {0}". format(s))