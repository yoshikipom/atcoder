import sys
from io import StringIO
import unittest
import math


def resolve():
    a, b, x = map(int, input().split())

    tan_theta = 2*(b/a-x/math.pow(a, 3))
    tan_theta2 = a * pow(b, 2) / (2 * x)

    if math.pow(a, 3) / 2 * tan_theta < x:
        theta = math.atan(tan_theta)
    else:
        theta = math.atan(tan_theta2)

    print(math.degrees(theta))


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
        input = """2 2 4"""
        output = """45.0000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12 21 10"""
        output = """89.7834636934"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1 8"""
        output = """4.2363947991"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
