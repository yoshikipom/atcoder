import sys
from io import StringIO
import unittest


def resolve():
    a, b, c, d = list(map(int, input().split()))
    blue = a
    red = 0
    for i in range(10**5 + 1):
        if blue <= red * d:
            print(i)
            return
        blue += b
        red += c
    print(-1)


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
        input = """5 2 3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 9 2 3"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
