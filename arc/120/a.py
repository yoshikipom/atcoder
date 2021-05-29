import sys
from io import StringIO
import unittest
import itertools


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    AA = list(itertools.accumulate(A))

    # print(A)
    # print(AA)

    max_a = 0
    accum_sum = 0

    for i in range(n):
        max_a = max(A[i], max_a)
        accum_sum += AA[i]
        result = max_a * (i+1) + accum_sum
        # print(max_a, accum_sum, result)
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
1 2 3"""
        output = """2
8
19"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
