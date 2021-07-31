import sys
from io import StringIO
import unittest
import bisect


def resolve():
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    result = float('inf')
    for a in A:
        b_index = bisect.bisect_left(B, a)
        result = min(result, abs(B[(b_index) % len(B)]-a))
        result = min(result, abs(B[(b_index-1) % len(B)]-a))
    for b in B:
        a_index = bisect.bisect_left(A, b)
        result = min(result, abs(A[(a_index) % len(A)]-b))
        result = min(result, abs(A[(a_index-1) % len(A)]-b))

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
        input = """2 2
1 6
4 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 8
82 76 82 82 71 70
17 39 67 2 45 35 22 24"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
