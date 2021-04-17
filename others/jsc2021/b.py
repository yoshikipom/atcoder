import sys
from io import StringIO
import unittest


def resolve():
    n, m = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    result = []
    for a in A:
        if a not in B:
            result.append(a)
    for b in B:
        if b not in A:
            result.append(b)

    result.sort()

    print(*result)


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
1 2
1 3"""
        output = """2 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 2 3 4
1 2 3 4"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
