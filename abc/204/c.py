import sys
from io import StringIO
import unittest
import sys

from collections import defaultdict

sys.setrecursionlimit(10000)


def resolve():
    n, m = list(map(int, input().split()))

    d = {}
    for i in range(n):
        d[i] = []

    for i in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        d[a].append(b)

    result = 0

    def dfs(cur, done):
        if cur in done:
            return

        done.add(cur)
        for next_city in d[cur]:
            dfs(next_city, done)

    for i in range(n):
        cur = i
        done = set()
        dfs(i, done)

        # print(i, len(done))
        result += len(done)

    print(result)


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
        input = """3 3
1 2
2 3
3 2"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 4
1 2
2 3
3 4
4 1"""
        output = """16"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
