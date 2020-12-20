import itertools
n = int(input())
A = list(map(int, input().split()))

A.sort()

B = list(itertools.accumulate(A))

result = 0
for i in range(n):
    result += B[-1] - B[i] - (A[i] * (n-i-1))

print(result)
