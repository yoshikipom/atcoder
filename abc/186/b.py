h, w = list(map(int, input().split()))
A = []

min_value = float('inf')
for _ in range(h):
    row = list(map(int, input().split()))
    A.append(row)
    min_value = min(min_value, min(row))

result = 0
for i in range(h):
    for j in range(w):
        result += A[i][j] - min_value

print(result)
