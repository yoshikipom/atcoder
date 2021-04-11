# TLE

from collections import deque
import sys
from io import StringIO
import unittest


def bfs(G, N, C):
    result = []

    dist = [-1]*N
    pan = [set() for i in range(N)]
    que = deque([0])
    dist[0] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in G[v]:
            if dist[w] > -1:
                continue
            pan[w] = pan[v] | {C[v]}
            dist[w] = d + 1
            que.append(w)
    # print(dist)
    # print(pan)

    for i in range(N):
        if C[i] not in pan[i]:
            print(i+1)


def resolve():
    n = int(input())
    C = list(map(int, input().split()))
    G = {}
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        if a not in G:
            G[a] = []
        if b not in G:
            G[b] = []
        G[a].append(b)
        G[b].append(a)

    bfs(G, n, C)


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
        input = """6
2 7 1 8 2 8
1 2
3 6
3 2
4 3
2 5"""
        output = """1
2
3
4
6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10"""
        output = """1
2
3
5
6
7
8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
