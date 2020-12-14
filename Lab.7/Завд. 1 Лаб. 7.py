coulmn = int(input("coulmn: "))
row = int(input("row: "))

import random
a = [[random.randint(-10,10) for j in range(row)] for i in range(coulmn)]
print("A =",a)

D = 1
i = False

for x in a[0::2]:
    for y in x[0::2]:
        if y < 0:
            i = True
            D *= y
if i:
    print("Добуток відємних елементів матриці з обома непарними індексами: {0}". format(D))
else:
    print("Добуток відємних елементів матриці з обома непарними індексами: 0")
