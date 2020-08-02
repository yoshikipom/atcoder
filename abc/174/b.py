cnt = 0
N, D = list(map(int, input().split()))
for _ in range(N):
    x, y = list(map(int, input().split()))
    if (x ** 2 + y ** 2) ** (1/2) <= D:
        cnt += 1

print(cnt)
