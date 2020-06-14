A = list(map(int, input().split()))
result = 0
for i in range(len(A)):
    if A[i] == 0:
        result = i + 1
        break

print(result)
