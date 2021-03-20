import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    n = len(s)
    if n == 1:
        print(0)
        return

    if n % 2 == 0:
        tmp = n // 2
        l = s[:tmp]
        r = s[tmp:]
    else:
        tmp = n // 2
        l = '9' * tmp
        r = '9' * tmp

    result = int(l)
    if (int(l) > int(r)):
        result -= 1

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
        input = """33"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1333"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000"""
        output = """999"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
