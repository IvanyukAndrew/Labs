n = int(input("Розмір матриці А і В: "))

import random
A = [[random.randint(-10,10) for j in range(n)]for i in range(n)]
B = [[random.randint(-10,10) for j in range(n)]for i in range(n)]

print("A =",A)
print("B =",B)

C = A + B

print("C =",C)

