X, N = list(map(int, input().split()))
P = list(map(int, input().split()))

P.sort()

result = 0
for i in range(0, 101):
    if X - i not in P:
        result = X - i
        break
    if X + i not in P:
        result = X + i
        break

print(result)
