import sys
from io import StringIO
import unittest


def resolve():
    a, b = list(map(int, input().split()))
    if 0 < a and b == 0:
        print('Gold')
    elif a == 0 and 0 < b:
        print('Silver')
    elif 0 < a and 0 < b:
        print('Alloy')
    else:
        raise Exception('error')


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
        input = """50 50"""
        output = """Alloy"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 0"""
        output = """Gold"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 100"""
        output = """Silver"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100 2"""
        output = """Alloy"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
