import sys
from io import StringIO
import unittest


def resolve():
    a, b = list(map(int, input().split()))
    print(b * a / 100)


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
        input = """45 200"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """37 450"""
        output = """166.5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 1000"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """50 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
