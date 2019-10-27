S = set()
for i in range(1, 10):
    for j in range(1, 10):
        S.add(i*j)

N = int(input())

if N in S:
    print('Yes')
else:
    print('No')
