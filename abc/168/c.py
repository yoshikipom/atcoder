import math

A, B, H, M = list(map(int, input().split()))

H_delta = H + M/60

xh = A * math.cos(2 * math.pi * H_delta/12)
yh = A * math.sin(2 * math.pi * H_delta/12)
xm = B * math.cos(2 * math.pi * M/60)
ym = B * math.sin(2 * math.pi * M/60)

dx = xh - xm
dy = yh - ym

result = (dx**2 + dy**2) ** (1/2)

print(result)
