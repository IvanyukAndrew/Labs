n = int(input("n = "))

count = 0

while n > 0:
    f=n%10
    if f==1:
        count+=1
    n=n//10
print("Кількість одиниць={0}".format(count))