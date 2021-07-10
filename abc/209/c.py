import sys
from io import StringIO
import unittest

MOD = 10**9 + 7


def resolve():
    n = int(input())
    C = list(map(int, input().split()))
    C.sort()

    result = 1
    for i in range(n):
        result *= C[i] - i
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
        input = """2
1 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
3 3 4 4"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
999999917 999999914 999999923 999999985 999999907 999999965 999999914 999999908 999999951 999999979"""
        output = """405924645"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
