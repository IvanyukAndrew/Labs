coulmn = int(input('coulmn: '))
row = int(input('row: '))

import random
A = [[random.randint(0, 10) for j in range(row)] for i in range(coulmn)]

index = 0
max_ = 0

print("Матриця: ")
for i in A:
    print(i)

for i in A:
    for x in i:
        if i.count(x) > max_:
            max_ = i.count(x)
            index = A.index(i)

print("Номер рядка з максимальною кількість одинак. елементів:", index + 1)