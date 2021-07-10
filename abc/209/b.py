import sys
from io import StringIO
import unittest


def resolve():
    n, x = list(map(int, input().split()))
    A = list(map(int, input().split()))
    price_sum = 0
    for i in range(n):
        if i % 2 != 0:
            price_sum += A[i] - 1
        else:
            price_sum += A[i]

    if price_sum <= x:
        print('Yes')
    else:
        print('No')


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
        input = """2 3
1 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 10
3 3 4 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 30
3 1 4 1 5 9 2 6"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
