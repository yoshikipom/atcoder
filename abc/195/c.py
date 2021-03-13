import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    tmp = n

    result = 0
    comma = 0
    base = 1
    while tmp >= 1000:
        tmp //= 1000
        comma += 1
        base *= 1000
        result += n - (base - 1)

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
        input = """1010"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """27182818284590"""
        output = """107730272137364"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
