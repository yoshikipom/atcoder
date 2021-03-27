import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    result = float('inf')
    for bit in range(1 << n):
        ors = []
        tmp = A[0]
        for i in range(n-1):
            if bit & (1 << i):
                ors.append(tmp)
                tmp = A[i+1]
            else:
                tmp |= A[i+1]
        ors.append(tmp)

        xors = 0
        for or_num in ors:
            xors ^= or_num
        result = min(result, xors)

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
1 5 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
10 10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 3 3 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
