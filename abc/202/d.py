import sys
from io import StringIO
import unittest
from math import factorial


def resolve():
    A, B, K = list(map(int, input().split()))
    N = A + B

    result = ''
    a = A
    b = B
    n = N
    k = K

    while n > 0:
        n -= 1
        if a <= 0:
            result += 'b'
            continue
        if b <= 0:
            result += 'a'
            continue

        # aだったパターンで過程
        a -= 1

        if a == 0 or b == 0:
            tmp = 1
        else:
            tmp = factorial(n) // factorial(a) // factorial(b)

        if k <= tmp:
            result += 'a'
        else:
            a += 1
            b -= 1
            k -= tmp
            result += 'b'

        # print('-------', n, a, b, k)

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
        input = """2 2 4"""
        output = """baab"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """30 30 118264581564861424"""
        output = """bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
