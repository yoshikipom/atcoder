N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

result = N - sum(A)

if result < 0:
    print(-1)
else:
    print(result)
