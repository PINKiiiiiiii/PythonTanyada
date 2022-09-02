n = int(input('Enter Your Loop: '))
A = []
for i in range(n):
    data = int(input('Enter Your Data: '))
    A += [data]
A.sort()
print(A[0])
print(A[-1])
