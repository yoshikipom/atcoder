import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    for i in range(n):
        result += A[i] * B[i]

    if result == 0:
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
        input = """2
-3 6
4 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
4 5
-1 -3"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 3 5
3 -6 3"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
