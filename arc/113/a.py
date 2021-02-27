import sys
from io import StringIO
import unittest
import math


def resolve():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        for j in range(1, n//i + 1):
            result += n // (i*j)

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
        input = """2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10"""
        output = """53"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31415"""
        output = """1937281"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
