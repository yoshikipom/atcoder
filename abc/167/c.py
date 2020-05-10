N, M, X = list(map(int, input().split()))

A = []
C = []
for _ in range(N):
    c, *row = list(map(int, input().split()))
    C.append(c)
    A.append(row)

INF = float('inf')
result = INF
for bit in range(1 << N):
    cost = 0
    spec = [0 for _ in range(M)]
    for i in range(N):
        if (bit >> i) & 1:
            cost += C[i]
            for j in range(M):
                spec[j] += A[i][j]

    # print(bin(bit), spec, cost)
    if min(spec) >= X:
        result = min(result, cost)

if result == INF:
    print(-1)
else:
    print(result)
