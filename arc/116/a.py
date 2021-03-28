import sys
from io import StringIO
import unittest


def resolve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 4 == 0:
            print('Even')
        elif n % 2 == 0:
            print('Same')
        else:
            print('Odd')


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
2
998244353
1000000000000000000"""
        output = """Same
Odd
Even"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
