import sys
from io import StringIO
import unittest
import math


def resolve():
    a, b, w = list(map(int, input().split()))
    w *= 1000

    diff = b-a

    tmp = w // a
    rest = w - a * tmp

    # print('max', tmp, rest)

    if rest/tmp > diff:
        print('UNSATISFIABLE')
        return
    else:
        result_max = tmp

    tmp = math.ceil(w / b)
    rest = b*tmp - w

    # print('min', tmp, rest)

    if rest/tmp > diff:
        print('UNSATISFIABLE')
        return
    else:
        result_min = tmp

    print(result_min, result_max)


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
        input = """100 200 2"""
        output = """10 20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """120 150 2"""
        output = """14 16"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """300 333 1"""
        output = """UNSATISFIABLE"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
