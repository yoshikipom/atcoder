A = list(map(int, input().split()))

result = False
for bit in range(2 ** 4):
    a = 0
    b = 0
    for i in range(4):
        if ((bit >> i) & 1):
            a += A[i]
        else:
            b += A[i]
    if a == b:
        result = True

if result:
    print('Yes')
else:
    print('No')
