from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True

def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

n, q = list(map(int, input().split()))

A = []
for i in range(1, n+1)[::-1]:
    A.append((i, 0))
    
Q = []
for _ in range(q):
    Q.append(input().split())
    
for op, c in Q:
    if op == '1':
        x, y = A[-1]
        if c == 'U':
            A.append((x, y+1))
        elif c == 'D':
            A.append((x, y-1))
        elif c == 'L':
            A.append((x-1, y))
        elif c == 'R':
            A.append((x+1, y))
    elif op == '2':
        p = int(c)
        print(*A[-p])
