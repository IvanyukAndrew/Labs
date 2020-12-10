n = int(input("Вкажіть кількість значень в масиві:"))
i = [int(input("i{0} = ".format(i+1))) for i in range(n)]

b1 = []
b2 = []

for el in i:
    if el >= 0:
        b1.append(el)
    else:
        b2.append(el)

b = b1 + b2

print("b = {0}".format(b))




