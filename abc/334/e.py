from collections import defaultdict
import math
import sys
import atcoder.math as am
from atcoder.dsu import DSU
sys.setrecursionlimit(10**6)

DEBUG = False
# DEBUG = True

MOD = 998244353
dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

def print_result(x,y):
    g = math.gcd(x,y)
    x//=g
    y//=g
    result = x * am.inv_mod(y, MOD)
    result %= MOD
    print(result)

h, w = list(map(int, input().split()))
M = []
for _ in range(h):
    M.append(input())

uf = DSU(h*w)
def index(i, j):
    return i*w+j

# 連結成分数を求める
greens = set()
for i in range(h):
    for j in range(w):
        if M[i][j] == '.':
            continue
        greens.add(index(i,j))
        for di, dj in dirs:
            if not 0<= i+di < h or not 0<= j+dj <w:
                continue
            if M[i+di][j+dj] == '.':
                continue
            uf.merge(index(i,j), index(i+di,j+dj))

link_cnt = 0
for group in uf.groups():
    if len(group) >= 2:
        link_cnt +=1
    elif len(group) == 1:
        if group[0] in greens:
            link_cnt += 1
            
debug(link_cnt)
debug('================')
x = 0
cnt_red = 0
for i in range(h):
    for j in range(w):
        if M[i][j] == '#':
            continue
        cnt_red += 1
        leader_set = set()
        for di, dj in dirs:
            if not 0 <= i+di < h or not 0 <= j+dj < w:
                continue
            if M[i+di][j+dj] == '.':
                continue
            leader_set.add(uf.leader(index(i+di,j+dj)))
        
        if len(leader_set) == 0:
            debug(i, j, link_cnt + 1)
            x+= link_cnt + 1
        else:
            debug(i, j, link_cnt-len(leader_set)+1, leader_set)
            x += link_cnt-len(leader_set)+1

print_result(x, cnt_red)  
