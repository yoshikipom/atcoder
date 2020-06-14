X, Y = list(map(int, input().split()))

result = 'No'
for i in range(0, 101):
    for j in range(0, 101):
        XX = i + j
        YY = i * 2 + j * 4
        if X == XX and Y == YY:
            result = 'Yes'

print(result)
