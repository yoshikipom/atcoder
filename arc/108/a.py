import collections


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


s, p = list(map(int, input().split()))
divs = make_divisors(p)

result = False
for a in divs:
    b = p/a
    # print(a, b)
    if a + b == s:
        result = True

if result:
    print('Yes')
else:
    print('No')
