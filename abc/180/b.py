N = int(input())
X = list(map(int, input().split()))
X = list(map(lambda x: abs(x), X))

result1 = 0
for x in X:
    result1 += abs(x)

result2 = 0
for x in X:
    result2 += x**2
result2 **= (1/2)

result3 = max(X)

print(result1)
print(result2)
print(result3)
