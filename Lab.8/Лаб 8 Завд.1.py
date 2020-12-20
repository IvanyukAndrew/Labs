def sum(n):
    sum1 = 0
    for i in range(1,6):
        sum1 += n**i
    return sum1

def v6(n):
    v8 = 1
    for i in range(1,6):
        v8 *=n**i
    return v8

def m(x):
    if x>0:
        return sum(x)
    else:
        return v6(x)

if "name"=="main":
    a = float(input("Ведіть а: "))
    b = float(input("Ведіть b: "))
    c = m(a) + m(2) + m(b)
    print("C =", c)