def S(a,b):
    import math
    s=(3-a)*math.sqrt(4*a+math.sin(math.sqrt(a**3)))
    return(s)

n=float(input("Значення інтеграла верхньої межі = "))
m=float(input("Значення інтеграла нижньої межі = "))

S=S(3,m)+S(n,m)
print("Значення S =",S)


