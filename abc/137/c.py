import unittest
from io import StringIO
import sys
from math import factorial
from scipy.misc import comb
import math


def resolve():
    N = int(input())
    d = {}
    count = 0
    for i in range(N):
        s = list(input())
        s.sort()
        s = ''.join(s)
        if s not in d.keys():
            d[s] = 1
        else:
            count += d[s]
            d[s] += 1

    print(count)


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
        input = """3
acornistnt
peanutbomb
constraint"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
oneplustwo
ninemodsix"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
