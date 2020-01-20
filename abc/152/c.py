import sys

N = int(input())
P = list(map(int, input().split()))

min_element = sys.maxsize
result = 0
for i in range(len(P)):
    if P[i] <= min_element:
        min_element = P[i]
        result += 1
    else:
        continue

print(result)
