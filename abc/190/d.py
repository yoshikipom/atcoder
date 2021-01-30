import sys
from io import StringIO
import unittest
import collections


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def resolve():
    n = int(input())
    # c = collections.Counter(prime_factorize(n))
    # if n % 2 == 0:
    # c[2] *

    result = 0
    divs = make_divisors(n)
    if n % 2 == 1:
        result = len(divs) * 2
    else:
        for div in divs:
            if div % 2 == 0 and n // div % 2 == 1:
                result += 1
            elif div % 2 == 1 and n // div % 2 == 0:
                result += 1
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
        input = """12"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """963761198400"""
        output = """1920"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
