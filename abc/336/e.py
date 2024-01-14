# WIP

from collections import defaultdict
import math
import sys
from atcoder.modint import ModContext, Modint
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True

def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

n = int(input())

# for i in range(1, n+1):
#     s = str(i)
#     total = 0
#     for c in s:
#         total += int(c)
    
#     if i % total == 0:
#         debug(i, total)
l = len(str(n))

if n < 10:
    print(n)
    sys.exit()

for total in range(1, 127):
    
    debug('total-> ', total)
    # dp = [[[0 for _ in range(total+1)] for _ in range(total+1)] for _ in range(l)]
    dp = [[0 for _ in range(total+1)] for _ in range(l)]
    for i in range(1, 10):
        if i <= total:
            # dp[0][i][0] += 1
            dp[0][i] += 1
        
    for i in range(l-1):
        for j in range(total+1):
            for k in range(10):
                if j + k > total:
                    continue
                # debug('plus', i, j, k)
                dp[i+1][j+k] += dp[i][j]
    for row in dp:
        debug(*row)
            
        