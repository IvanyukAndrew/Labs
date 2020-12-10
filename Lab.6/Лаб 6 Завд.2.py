import math

n=int(input("Введіть кількість елементів n: "))
a = []
i=1
for i in range(n):
    if i<=n:
        a += [(-1+2-3+(-1)**i*i)/(math.factorial(i))]
        i=i+1

A=a
print("Масив A={0}".format(a))

S = 0
for i in range(n):
    if a[i]>0:
        S=S+a[i]
print("Сума додатніх елементів масиву А = {0}".format(S))


