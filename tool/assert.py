from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
# DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)


"""
a + b + c = N
2a + 3b + 4c = M
-> b + 2c = M - 2N
"""

n, m = list(map(int, input().split()))

for b in range(0, 2*m-n):
    debug(b)
    tmp = m-2*n - b
    if tmp % 2 != 0:
        debug(tmp, 'not *2')
        continue
    c = tmp//2
    a = n - b - c
    if a < 0:
        debug(a, ' < 0', b, c)
        continue
    
    print(a, b, c)
    if a + b + c != n or 2*a + 3*b + 4*c != m:
        sys.exit(1)
    sys.exit()

print(-1, -1, -1)
sys.exit(1)
