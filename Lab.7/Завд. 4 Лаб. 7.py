coulmn = int(input('coulmn : '))
row = int(input('row : '))

import random
A = [[random.randint(0, 100) for j in range(row)] for i in range(coulmn)]

print(A)

for i in range(coulmn):
   for j in range(row):
        if i % 2 == 0:
            A[i].sort()

print('\n')
print(A)