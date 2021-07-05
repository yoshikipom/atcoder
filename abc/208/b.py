import sys
from io import StringIO
import unittest
import math


def resolve():
    p = int(input())
    count = 0
    for i in reversed(range(1, 11)):
        a = math.factorial(i)
        if p >= a:
            count += p // a
            p %= a

    print(count)


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
        input = """9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """119"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000"""
        output = """24"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
