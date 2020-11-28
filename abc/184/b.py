n, x = list(map(int, input().split()))
s = input()
result = x
for c in s:
    if c == 'o':
        result += 1
    else:
        if result > 0:
            result -= 1

print(result)
