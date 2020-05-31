N = int(input())
A = []
B = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N % 2 == 1:
    print(B[N//2] - A[N//2] + 1)
else:
    a0 = A[N//2 - 1]
    b0 = B[N//2 - 1]
    a1 = A[N//2]
    b1 = B[N//2]

    print((b1 + b0) - (a1 + a0) + 1)
