A = []
L = 10

for C in range(L):
    name = input("Enter your name : ")
    A[C] = name

for C in range(L):
    for i in range(9):
        if A[i] < A[i + 1]:
            T = A[i]
            A[i] = A[i + 1]
            A[i + 1] = T

for C in range(L):
    print(A[C])
