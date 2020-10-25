n = int(input())

result = None
for i in range(1, 40):
    for j in range(1, 30):
        if 3 ** i + 5 ** j == n:
            result = (i, j)

if result:
    print(*result)
else:
    print(-1)
