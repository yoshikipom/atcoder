N = int(input())

tmp = N % 1000

result = 1000 - tmp

if result == 1000:
    print(0)
else:
    print(result)
