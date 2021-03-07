import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    result = 0
    for j in range(2, n+1):
        result += n/(j-1)
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
        input = """2"""
        output = """2.00000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3"""
        output = """4.50000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
