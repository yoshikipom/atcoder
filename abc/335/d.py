from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
# DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)


n = int(input())

A = [[None for i in range(n)]for _ in range(n)]
A[(n)//2][(n)//2] = 'T'

i = 0
j = 0
dir_cur = 0
dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

num = 1
while num < n**2:
    debug(i, j)
    A[i][j] = num
    num += 1
    
    di, dj = dirs[dir_cur]
    ii = i+di
    jj = j+dj
    if not 0<=ii<n or not 0<=jj<n or A[ii][jj]!=None:
        dir_cur += 1
        dir_cur %= 4
        di, dj = dirs[dir_cur]
        ii = i+di
        jj = j+dj
    i = ii
    j = jj
        
for row in A:
    print(*row)
        
    
