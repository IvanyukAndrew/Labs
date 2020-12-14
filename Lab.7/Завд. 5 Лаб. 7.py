coulmn = int(input('coulmn : '))
row = int(input('row : '))

import random
A = [[random.randint(-10, 10) for j in range(row)] for i in range(coulmn)]

k = 1
SumRow = 0
for i in range(coulmn):
    for j in range(row):
        if A[i][j] == False:
            k = False
            SumRow += 1
            k = 1

print(A)
print(SumRow)