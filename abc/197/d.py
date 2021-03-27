import sys
from io import StringIO
import unittest
import math


def resolve():
    n = int(input())
    x0, y0 = list(map(int, input().split()))
    xn2, yn2 = list(map(int, input().split()))

    xc = (x0 + xn2)/2
    yc = (y0 + yn2)/2

    x0t = x0-xc
    y0t = y0-yc

    distance = (x0t**2 + y0t**2) ** 0.5
    deg = 360/n + math.degrees(math.atan2(y0t, x0t))

    # print(deg, 360/n, math.degrees(math.atan2(y0t, x0t)))

    x1 = distance * math.cos(math.radians(deg))
    y1 = distance * math.sin(math.radians(deg))

    # print(x1, y1)
    # print(distance, x0t, y0t)

    print(x1 + xc, y1 + yc)


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
        input = """4
1 1
2 2"""
        output = """2.00000000000 1.00000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
5 3
7 4"""
        output = """5.93301270189 2.38397459622"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
