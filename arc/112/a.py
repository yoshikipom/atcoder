import sys
from io import StringIO
import unittest


def solve(l, r):
    if l != 0 and r < 2*l:
        print(0)
        return
    x = r - 2 * l + 1
    result = (1 + x) * x // 2
    print(result)


def resolve():
    t = int(input())
    for _ in range(t):
        l, r = list(map(int, input().split()))
        solve(l, r)


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
        input = """5
2 6
0 0
1000000 1000000
12345 67890
0 1000000"""
        output = """6
1
0
933184801
500001500001"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
