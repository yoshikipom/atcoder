import sys
from io import StringIO
import unittest


def resolve():
    n, k = list(map(int, input().split()))
    a = n
    for i in range(k):
        s = str(a)
        C = []
        for c in s:
            C.append(c)
        C.sort()
        g1 = int(''.join(C))
        g2 = int(''.join(sorted(C, reverse=True)))
        a = g2-g1

    print(a)


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
        input = """314 2"""
        output = """693"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6174 100000"""
        output = """6174"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
