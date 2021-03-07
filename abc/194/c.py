import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    formula1 = (n-1) * sum(map(lambda x: x**2, A))

    tmp = 0
    tmp_sum = sum(A)
    for i in range(n):
        a = A[i]
        tmp_sum -= a
        tmp += a * tmp_sum
    formula2 = -2 * tmp

    print(formula1 + formula2)


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
2 8 4"""
        output = """56"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
-5 8 9 -4 -3"""
        output = """950"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
