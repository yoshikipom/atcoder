N = int(input())
result = 0
A = list(map(int, input().split()))

result = 0
for i, a in enumerate(A):
    if (i + 1) % 2 == 0:
        continue
    if a % 2 != 0:
        result += 1

print(result)
