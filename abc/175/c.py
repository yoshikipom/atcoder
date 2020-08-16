x, k, d = list(map(int, input().split()))
x = abs(x)

if k * d <= x:
    print(x - k * d)
else:
    k -= x//d
    x %= d
    if k % 2 == 0:
        print(x)
    else:
        print(abs(x-d))
