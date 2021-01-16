import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    mid = (2**n)//2
    A1 = A[:mid]
    A2 = A[mid:]
    max1 = max(A1)
    max2 = max(A2)

    if max1 < max2:
        print(A1.index(max1)+1)
    else:
        print(A2.index(max2) + mid + 1)


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
1 4 2 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
3 1 5 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
