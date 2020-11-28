a, b, x, y = list(map(int, input().split()))

INF = float('inf')
dpa = [INF for _ in range(101)]
dpb = [INF for _ in range(101)]

dpa[a] = 0
dpb[a] = x
if a <= b:

    for i in range(a, b):
        dpa[i + 1] = min(dpa[i] + y, dpb[i] + x)
        dpb[i + 1] = min(dpa[i+1] + x, dpb[i] + y)
else:
    for i in range(a, b, -1):
        dpb[i - 1] = min(dpa[i] + x, dpb[i] + y)
        dpa[i - 1] = min(dpa[i] + y, dpb[i-1] + x)

print(dpb[b])
