def sum_func(n):
    sum = 0
    for i in range(1,6):
        sum += n**i
    return sum

def prod_func(num):
    prod = 1
    for i in range(1,6):
        prod *= num**i
    return prod

def m_func(x):
    if x>0:
        return sum_func(x)
    else:
        return prod_func(x)

a = float(input("Ведіть а: "))
b = float(input("Ведіть b: "))
c = m_func(a) + m_func(2) + m_func(b)
print("C =", c)
