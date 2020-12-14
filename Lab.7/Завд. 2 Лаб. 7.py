coulmn = int(input("coulmn: "))
row = int(input("row: "))

import random
a = [[random.randint(0,4) for j in range(row)] for i in range(coulmn)]
print(a)

for i in range(coulmn):
    for j in range(row):
        if a[i][j]<3:
            a[i][j] = i + j
        else:
            a[i][j] = -1 + 2 + (-1)**j*j
print(a)

b = []
for i in range(coulmn):
    for j in range(row):
        b.append(a[i][j])
print(b)
