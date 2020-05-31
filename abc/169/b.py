N = int(input())
A = list(map(int, input().split()))

result = 1
ok = True
if 0 in A:
    result = 0
else:
    for a in A:
        result *= a
        if result > 10 ** 18:
            ok = False
            break

if ok:
    print(result)
else:
    print(-1)
