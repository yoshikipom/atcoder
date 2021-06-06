import sys
from io import StringIO
import unittest


def resolve():
    n = list(map(int, input().split()))
    A = list(map(int, input().split()))

    result = 0
    for a in A:
        if a > 10:
            result += a - 10

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
6 17 28"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
8 9 10 11"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
