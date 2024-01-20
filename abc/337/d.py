from collections import defaultdict
from itertools import accumulate
import math
import sys
import numpy as np
sys.setrecursionlimit(10**6)

DEBUG = False
# DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

H, W, K = list(map(int, input().split()))
M = []
for _ in range(H):
    M.append(input())
    
INF = float('inf')
result = INF

for row in M:
    debug(*row)

for i in range(H):
    acc_a = [0]
    val = 0
    for j in range(W):
        if M[i][j] == 'o':
            val += 1
        acc_a.append(val)
        
    acc_b = [0]
    val = 0
    for j in range(W):
        if M[i][j] == '.':
            val += 1
        acc_b.append(val)
    
    debug(i, acc_a, acc_b)
    for l in range(W-K+1):
        r = l+K
        debug(l, r)
        a = acc_a[r] - acc_a[l]
        b = acc_b[r] - acc_b[l]
        if a + b != K:
            continue
        debug('result found', i, l, a, b)
        result = min(result, b)


debug('=======vertical=========')
for j in range(W):
    acc_a = [0]
    val = 0
    for i in range(H):
        if M[i][j] == 'o':
            val += 1
        acc_a.append(val)

    acc_b = [0]
    val = 0
    for i in range(H):
        if M[i][j] == '.':
            val += 1
        acc_b.append(val)

    debug(i, acc_a, acc_b)
    for l in range(H-K+1):
        r = l+K
        debug(l, r)
        a = acc_a[r] - acc_a[l]
        b = acc_b[r] - acc_b[l]
        if a + b != K:
            continue
        debug('result found', i, l, a, b)
        result = min(result, b)
        
            
if result == INF:
    print(-1)
else:
    print(result)
