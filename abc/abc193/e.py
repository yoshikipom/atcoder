import sys
from io import StringIO
import unittest
import math

INF = float('inf')


def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0


def crt(a, mods):
    rem, m = 0, 1
    for i in range(len(a)):
        g, p, q = extgcd(m, mods[i])
        if (a[i] - rem) % g != 0:
            return 0, -1
        tmp = (a[i] - rem) // g * p % (mods[i] // g)
        rem += m * tmp
        m *= mods[i] // g
    return rem % m, m


def solve():
    x, y, p, q = list(map(int, input().split()))
    result = INF
    mods = (p + q, 2 * x + 2 * y)
    for i in range(p, p + q):
        for j in range(x, x+y):
            a = (i, j)
            rem, M = crt(a, mods)
            if M != -1:
                result = min(rem, result)

    if result == INF:
        print("infinity")
    else:
        print(result)


def resolve():
    t = int(input())
    for _ in range(t):
        solve()


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
5 2 7 6
1 1 3 1
999999999 1 1000000000 1"""
        output = """20
infinity
1000000000999999999"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
