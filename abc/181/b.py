def sum_range(a, b):
    cnt = b - a + 1
    return (b+a) / 2 * cnt


n = int(input())
result = 0
for _ in range(n):
    a, b = list(map(int, input().split()))
    result += sum_range(a, b)

print(int(result))
