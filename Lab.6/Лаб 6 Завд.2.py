import math

n=int(input("Введіть кількість елементів n: "))
a = []
b = 0
for i in range(1, n+1):
    b = b + ((-1)**i)*i
    a.append(b/math.factorial(i))

print("Масив A={0}".format(a))

S = 0
for el in a:
    if el>0:
        S=S+el
print("Сума додатніх елементів масиву А = {0}".format(S))
