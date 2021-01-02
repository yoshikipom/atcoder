import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    X = []
    Y = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        X.append(x)
        Y.append(y)
    result = 0
    for i in range(n-1):
        for j in range(i+1, n):
            dy = Y[i] - Y[j]
            dx = X[i] - X[j]
            if dx == 0:
                continue
            # print(dy / dx)
            if -1 <= dy / dx and dy / dx <= 1:
                result += 1
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
        input = """3
0 0
1 2
2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
-691 273"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
-31 -35
8 -36
22 64
5 73
-14 8
18 -58
-41 -85
1 -88
-21 -85
-11 82"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
