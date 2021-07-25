import sys
from io import StringIO
import unittest


def resolve():
    a, b = list(map(int, input().split()))
    result = (a-b) / 3 + b
    print(result)


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
        input = """130 100"""
        output = """110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """300 50"""
        output = """133.3333333"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123 123"""
        output = """123"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
