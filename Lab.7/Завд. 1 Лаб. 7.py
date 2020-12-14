coulmn = int(input("coulmn: "))
row = int(input("row: "))

import random
a = [[random.randint(-10,10) for j in range(row)] for i in range(coulmn)]

S = 0

for i in range(coulmn):
    for j in range(row):
        if i % 2 == 1 and j % 2 == 1 and a[i][j] < 0:
            S = S * a[i][j]
print("Добуток відємних елементів матриці з обома непарними індексами: {0}". format(S))
