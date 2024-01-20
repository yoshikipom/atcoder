from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)


n = int(input())
A = list(map(int, input().split()))

d = {}
for i, a in enumerate(A):
    d[a] = i+1

result = []
cur = -1
for i in range(n):
    result.append(d[cur])
    cur = d[cur]

print(*result)
