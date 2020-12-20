import random

n = int(input('Введіть n: '))
A = [[random.randint(-5, 5) for j in range(n)] for i in range(n)]

for i in A:
    print(i)

for num in range(n):
    if num % 2 != 0:
        st = []
        for num_r in range(n):
            st.append(A[num_r][num])
        st.sort()
        for num_r in range(n):
            A[num_r][num] = st[num_r]

print("А :")
for i in A:
    print(i)
