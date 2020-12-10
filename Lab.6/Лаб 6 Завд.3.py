n = int(input("Вкажіть вимір вектора:"))
a = [float(input("Задайте  координату вектора x{0} = ".format(i+1))) for i in range(n)]
b = [float(input("Задайте  координату вектора y{0} = ".format(i+1))) for i in range(n)]

d = 0
for el in range(n):
    d=a[el]*b[el]+d
print(d)

