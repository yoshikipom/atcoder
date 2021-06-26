import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    comb = n * (n-1) // 2

    d = {}
    for a in A:
        if a not in d:
            d[a] = 0
        d[a] += 1

    for k, v in d.items():
        comb -= v * (v-1) // 2

    print(comb)


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
1 7 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
1 10 100 1000 10000 100000 1000000 10000000 100000000 1000000000"""
        output = """45"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4"""
        output = """173"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
