n = int(input())
L = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = L[i]
            b = L[j]
            c = L[k]
            if a == b or b == c or c == a:
                continue
            if a+b > c and b+c > a and c+a > b:
                result += 1
                # print(i, j, k)

print(result)
