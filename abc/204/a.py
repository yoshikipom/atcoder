import sys
from io import StringIO
import unittest


def resolve():
    x, y = list(map(int, input().split()))
    S = set()
    S.add(x)
    S.add(y)

    if len(S) == 1:
        print(x)
    else:
        if 0 not in S:
            print(0)
        elif 1 not in S:
            print(1)
        else:
            print(2)


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
        input = """0 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
