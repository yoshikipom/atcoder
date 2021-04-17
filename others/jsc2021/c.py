import sys
from io import StringIO
import unittest


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def resolve():
    A, B = list(map(int, input().split()))
    mid = (A+B)//2 + 1

    result = 1
    for i in range(A, mid+1):
        divs = make_divisors(i)
        for div in divs:
            if i + div <= B:
                result = max(result, div)

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
        input = """2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """199999 200000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """101 139"""
        output = """34"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
