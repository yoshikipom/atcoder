N = int(input())
A = list(map(int, input().split()))
result = [0] * (N + 1)
for i in range(1, N+1):
    result[A[i - 1]] = i

print(' '.join(map(str, result[1::])))
