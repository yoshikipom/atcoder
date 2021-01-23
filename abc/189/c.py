import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    result = 0
    for l in range(n):
        x = A[l]
        for r in range(l, n):
            x = min(x, A[r])
            result = max(result, x * (r - l + 1))
            # print(l, r, x, x * (r - l + 1))

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
        input = """6
2 4 4 9 4 9"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
200 4 4 9 4 9"""
        output = """200"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
