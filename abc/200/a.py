import sys
from io import StringIO
import unittest
import math


def resolve():
    n = int(input())

    print(math.ceil(n/100))


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
        input = """2021"""
        output = """21"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """200"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
