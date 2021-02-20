import sys
from io import StringIO
import unittest
import math

from heapq import heappush, heappop
INF = float('inf')


def dijkstra(s, n, adj):
    dist = [INF] * n
    dist[s] = 0
    hq = [(0, s, 0)]
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost, k in adj[v]:
            time = math.ceil(dist[v]/k) * k
            if seen[to] == False and cost + time < dist[to]:
                dist[to] = cost + time
                heappush(hq, (dist[to], to))
    return dist


def resolve():
    n, m, x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b, t, k = list(map(int, input().split()))
        a -= 1
        b -= 1
        adj[a].append((b, t, k))
        adj[b].append((a, t, k))

    res = dijkstra(x, n, adj)[y]
    if res == INF:
        print(-1)
    else:
        print(res)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 2 1 3
1 2 2 3
2 3 3 4"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2 3 1
1 2 2 3
2 3 3 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 0 3 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """9 14 6 7
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3
2 3 8 4
6 2 6 4
3 8 3 2
7 9 5 2
8 4 1 9
7 1 6 9
3 9 9 3
7 5 1 5
8 2 9 7
4 9 4 4"""
        output = """26"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
