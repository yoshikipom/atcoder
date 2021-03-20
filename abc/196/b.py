import sys
from io import StringIO
import unittest


def resolve():
    x = input()
    print(x.split('.')[0])


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
        input = """5.90"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """84939825309432908832902189.9092309409809091329"""
        output = """84939825309432908832902189"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
