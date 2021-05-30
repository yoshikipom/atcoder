import sys
from io import StringIO
import unittest


def resolve():
    a, b, c = list(map(int, input().split()))
    if a != b and b != c and c != a:
        print(0)
        return

    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)


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
        input = """2 5 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1 1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
