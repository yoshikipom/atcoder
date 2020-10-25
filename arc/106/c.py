
import sys
n, m = list(map(int, input().split()))

if m == 0:
    for i in range(1, n+1):
        print(i*2 - 1, i*2)
    sys.exit()

if m < 0 or n - 2 < m:
    print(-1)
    sys.exit()


print(1, 2*(m+2))
for i in range(m+1):
    print(2 * i + 2, 2 * i + 3)

for i in range(m + 3, n+1):
    print(i*2 - 1, i*2)
