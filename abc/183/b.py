sx, sy, gx, gy = list(map(int, input().split()))

a = (gy + sy)/(gx - sx)
b = gy - a*gx
result = -b/a

print(result)
