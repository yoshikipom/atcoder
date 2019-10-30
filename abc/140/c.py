N = int(input())
B = list(map(int, input().split()))
B.append(B[-1])

result = 0
result += B[0]
for i in range(1, N-1):
    result += min(B[i], B[i-1])
result += B[N-2]

print(result)
