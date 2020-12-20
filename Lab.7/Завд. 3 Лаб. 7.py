n = int(input("Розмір матриці А і В: "))

import random
A = [[random.randint(-10,10) for j in range(n)]for i in range(n)]
B = [[random.randint(-10,10) for j in range(n)]for i in range(n)]
C = [[x+y for x,y in zip(i,j)]for i,j in zip(A,B)]

print("Матриця A: ")
for i in A:
    print(i)

print("Матриця B: ")
for i in B:
    print(i)

print("Матриця C: ")
for i in C:
    print(i)
