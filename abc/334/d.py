import bisect
from collections import defaultdict
import itertools
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
# DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

n, q = list(map(int, input().split()))
R = list(map(int, input().split()))
R.sort()
A = [0] + list(itertools.accumulate(R))

debug(A)

Q = []
for _ in range(q):
    Q.append(int(input()))
    
for x in Q:
    index = bisect.bisect_right(A, x)
    print(index-1)
