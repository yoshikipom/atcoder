import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    s1 = s[1:]
    s2 = s[0]
    print(s1+s2)


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
        input = """abc"""
        output = """bca"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aab"""
        output = """aba"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
