import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


n = int(input())

tmp = 1
for i in range(2, n+1):
    tmp = lcm(tmp, i)

print(tmp+1)
