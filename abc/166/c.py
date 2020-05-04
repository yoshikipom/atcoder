N, M = list(map(int, input().split()))
H = list(map(int, input().split()))

d = {}
for i in range(N):
    d[i] = set()

for _ in range(M):
    A, B = list(map(int, input().split()))
    d[A-1].add(B-1)
    d[B-1].add(A-1)

cnt = 0
for i in range(N):
    good = True
    for neighbor in d[i]:
        if H[neighbor] >= H[i]:
            good = False

    if good:
        cnt += 1
        # print('good', i)

print(cnt)
