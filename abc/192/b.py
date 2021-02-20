import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    difficult = True
    for c in s[::2]:
        if not c.islower():
            difficult = False
    for c in s[1::2]:
        if not c.isupper():
            difficult = False

    if difficult:
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
        input = """dIfFiCuLt"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """eASY"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """a"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
