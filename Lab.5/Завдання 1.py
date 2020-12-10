a = float(input("a = "))
n = float(input("n = "))

S = a**2
i = 1

while i<=n-1:
    S = S*(a+n-i)**2
    i = i+1
else:
    print(S)