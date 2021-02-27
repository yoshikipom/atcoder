import sys
from io import StringIO
import unittest


def point(given, arg):
    score = 0
    for i in range(1, 10):
        num = given[i]
        if (i == arg):
            num += 1
        score += i * pow(10, num)
    return score


def resolve():
    k = int(input())
    s = input()
    t = input()
    S = [int(s[i]) for i in range(4)]
    T = [int(t[i]) for i in range(4)]

    rest = {}
    taka = {}
    aoki = {}
    for i in range(1, 10):
        rest[i] = k
        taka[i] = 0
        aoki[i] = 0
    for i in range(4):
        rest[S[i]] -= 1
        taka[S[i]] += 1
        rest[T[i]] -= 1
        aoki[T[i]] += 1

    result = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                if rest[i] <= 1:
                    continue
                p = rest[i] * (rest[i] - 1)
            else:
                if rest[i] <= 0 or rest[j] <= 0:
                    continue
                p = rest[i] * rest[j]

            if point(taka, i) > point(aoki, j):
                result += p

    result /= (9*k-8) * (9*k-9)
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
        input = """2
1144#
2233#"""
        output = """0.4444444444444444"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
9988#
1122#"""
        output = """1.0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1122#
2228#"""
        output = """0.001932367149758454"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000
3226#
3597#"""
        output = """0.6296297942426154"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
