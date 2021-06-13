import sys
from io import StringIO
import unittest


def resolve():
    a, b, c = list(map(int, input().split()))

    if c % 2 == 0:
        if abs(a) < abs(b):
            print('<')
        elif abs(a) == abs(b):
            print('=')
        else:
            print('>')
    else:
        if a >= 0 and b >= 0:
            if a < b:
                print('<')
            elif a == b:
                print('=')
            else:
                print('>')
        elif a >= 0 and b < 0:
            print('>')
        elif a < 0 and b >= 0:
            print('<')
        elif a < 0 and b < 0:
            if a < b:
                print('<')
            elif a == b:
                print('=')
            else:
                print('>')
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
        input = """3 2 4"""
        output = """>"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-7 7 2"""
        output = """="""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """-8 6 3"""
        output = """<"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
