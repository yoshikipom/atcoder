from atcoder.dsu import DSU
from collections import deque
from collections import defaultdict
import math
import sys
from typing import Tuple
sys.setrecursionlimit(10**6)

DEBUG = False
# DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)


class TopologicalGraph:
    def __init__(self, n: int):
        self.n = n
        self.degree = [0] * n
        self.d = defaultdict(list)

    def add_edge(self, src, dist):
        self.degree[dist] += 1
        self.d[src].append(dist)

    # return sorted array and longest path length
    def sort(self) -> Tuple[list[int], int]:
        ans = []
        q = deque()  # index, degree
        for i in range(self.n):
            if self.degree[i] == 0:
                q.appendleft((i, 0))
                ans.append(i)

        longest = 0
        while q:
            v, cnt = q.pop()
            longest = max(longest, cnt)
            for t in self.d[v]:
                self.degree[t] -= 1
                if self.degree[t] == 0:
                    q.appendleft((t, cnt+1))
                    ans.append(t)

        return ans, longest


n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
uv = []
for _ in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    uv.append((u, v))


uf = DSU(n)
for u, v in uv:
    if A[u] == A[v]:
        uf.merge(u, v)

m = {}
for i in range(n):
    m[i] = uf.leader(i)

d = defaultdict(list)
for u, v in uv:
    if A[u] < A[v]:
        d[m[u]].append(m[v])
    elif A[u] > A[v]:
        d[m[v]].append(m[u])

for key in d.keys():
    d[key] = list(set(d[key]))

dp = [-1 for i in range(n)]

g = TopologicalGraph(n)
for key, arr in d.items():
    for v in arr:
        g.add_edge(key, v)

B, longest = g.sort()

dp[m[0]] = 1
debug(m)
debug(d)
debug(B)
for i in B:
    debug(i, dp)

    if dp[m[i]] == -1:
        continue
    for next_cur in d[m[i]]:
        if m[next_cur] == m[i]:
            continue
        dp[m[next_cur]] = max(dp[m[next_cur]], dp[m[i]]+1)
        
if dp[m[n-1]] == -1:
    print(0)
else:
    print(dp[m[n-1]])
