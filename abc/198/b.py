import sys
from io import StringIO
import unittest


def resolve():
    n = input()
    result = False

    if n == n[::-1]:
        result = True
    for _ in range(len(n)):
        n = '0' + n
        if n == n[::-1]:
            result = True

    if result:
        print('Yes')
    else:
        print('No')


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
        input = """1210"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """777"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123456789"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
