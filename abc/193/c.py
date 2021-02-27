import sys
from io import StringIO
import unittest
import math


def resolve():
    n = int(input())

    S = set()

    for i in range(2, math.floor(n**0.5)+1):
        b = 2
        while i ** b <= n:
            S.add(i**b)
            b += 1

    print(n-len(S))


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
        input = """8"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000"""
        output = """99634"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
