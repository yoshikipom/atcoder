import sys
from io import StringIO
import unittest


def resolve():
    A = list(map(int, input().split()))
    print(sum(A) - min(A))


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
        input = """3 4 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 6 6"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """99 99 98"""
        output = """198"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
