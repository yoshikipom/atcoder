import sys
from io import StringIO
import unittest
import math


def resolve():

    t, n = list(map(int, input().split()))

    # for i in range(1, 201):
    #     taxed = math.floor((100 + t) / 100 * i)
    #     print(i, taxed, i * (100 + t) / 100)

    base = math.ceil(n * 100/t)
    print(base + n - 1)


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
        input = """10 1"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5"""
        output = """171"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1000000000"""
        output = """100999999999"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
