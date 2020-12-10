import math
x = float(input("x від 0 до числа п = "))
if not(0<x<math.pi):
    print("Program EROR")
    exit(0)
e = float(input("e = "))
n = 1
s1 = math.log1p(math.fabs(math.sin(x)))
S = -math.log1p(2)

while math.fabs(S)<e:
    S-=(math.cos(2*n*x)/n)
    n=n+1

if S-s1<e:
    print("Справедливо")
else:
    print("Несправедливо")

