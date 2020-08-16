s = input()
result = 0
tmp = 0
for c in s:
    if c == 'R':
        tmp += 1
    else:
        tmp = 0
    result = max(result, tmp)

print(result)
