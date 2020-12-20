def count(f=10):
    if f==0:
        return 1
    else:
        return count(f-1)+2*f
print("x10 =",count())
