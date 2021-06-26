import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())

    money = 0
    for i in range(1, 10**9 + 1):
        money += i
        if money >= n:
            break

    print(i)


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
        input = """12"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100128"""
        output = """447"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
