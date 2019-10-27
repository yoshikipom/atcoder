from math import factorial


def comb(n, r):
    if n == 0 or n-r < 0:
        return 0
    return int(factorial(n) / factorial(r) / factorial(n-r))


N = int(input())
S = []
for i in range(N):
    s = list(input())
    s.sort()
    S.append(s)

S.sort()

count = 0
count_min = 0
tmp = []
for s in S:
    if s == tmp:
        count_min += 1
    else:
        count += comb(count_min+1, 2)
        count_min = 0
    tmp = s
    # print('count:{}, min:{}'.format(count, count_min))
count += comb(count_min+1, 2)
print(count)
