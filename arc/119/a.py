import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())

    result = float('inf')
    for i in range(60):
        a = n // (2 ** i)
        b = i
        c = n % (2 ** i)

        # print(i, a, b, c)

        result = min(result, a+b+c)

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
        input = """998244353"""
        output = """143"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000007"""
        output = """49483"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """998984374864432412"""
        output = """2003450165"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
