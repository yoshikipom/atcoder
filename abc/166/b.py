N, K = list(map(int, input().split()))

A = [[False for _ in range(K)] for _ in range(N)]
for i in range(K):
    d = int(input())
    row = list(map(int, input().split()))
    for j in row:
        A[j-1][i] = True

cnt = 0
for row in A:
    if not any(row):
        cnt += 1

print(cnt)
