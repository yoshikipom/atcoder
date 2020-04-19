from collections import OrderedDict

d = OrderedDict()

N = int(input())

for i in range(N):
    d[i] = 0

A = list(map(int, input().split()))
for a in A:
    d[a-1] += 1

for key, value in d.items():
    print(value)
