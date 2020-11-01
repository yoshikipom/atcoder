n = int(input())
ps = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    ps.append((x, y))

line_set = set()
result = False
for i in range(n-1):
    for j in range(i + 1, n):
        x1, y1 = ps[i]
        x2, y2 = ps[j]
        if x2-x1 != 0:
            a = (y2-y1) / (x2-x1)
            b = y1 - a * x1
            b2 = y2 - a * x2
            # print(a, b, b2)
        else:
            a = x1
            b = None
            # print(x1, x2)
        if (a, b) in line_set:
            result = True
            break
        else:
            line_set.add((a, b))

if result:
    print('Yes')
else:
    print('No')
