import sys
from io import StringIO
import unittest


def resolve():
    a, b, c = list(map(int, input().split()))
    print(21-a-b-c)


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
        input = """1 4 3"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 6 4"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
