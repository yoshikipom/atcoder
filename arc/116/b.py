import unittest
from io import StringIO
import sys


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    A.sort()

    result = 0
    MOD = 998244353
    if n == 1:
        print((A[0] * A[0]) % MOD)
        return

    result += A[0]*A[0] + A[0] * A[1] + A[1] * A[1]

    if n == 2:
        print(result % MOD)
        return

    min_sum = A[0] + A[1]
    for i in range(2, n):
        min_sum = 2 * (min_sum) - A[i-1] + A[i]
        min_sum %= MOD
        result += A[i] * min_sum
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
        input = """3
2 4 3"""
        output = """63"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
10"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
853983 14095 543053 143209 4324 524361 45154"""
        output = """206521341"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
