import math


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


l = int(input())
print(comb(l-1, 11))
