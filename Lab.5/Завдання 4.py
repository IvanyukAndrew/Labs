n=int(input("Введіть номер n-го елемента: "))
a = [1,1]
i=2
while i<=n:
    el=a[i-1]+a[i-2]
    a.append(el)
    i=i+1
print("Список",a)
print("xn={0}".format(el))