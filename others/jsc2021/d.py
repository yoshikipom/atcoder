import sys
from io import StringIO
import unittest

MOD = 10 ** 9 + 7


def resolve():
    n, p = list(map(int, input().split()))
    q = p-1

    if q == 1:
        if n == 1:
            print(1)
        else:
            print(0)
    else:
        # a = pow(q, n, MOD)
        # b = (pow(q, n-1, MOD) - 1) // (q - 1)
        # result = a - q * b
        # result %= MOD

        result = q * pow(q-1, n-1, MOD)
        result %= MOD

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
        input = """3 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """45108 2571593"""
        output = """224219544"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
