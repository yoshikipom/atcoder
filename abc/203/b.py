import sys
from io import StringIO
import unittest


def range_sum(num):
    return sum(list(range(1, num+1)))


def resolve():
    n, k = list(map(int, input().split()))

    result = 0
    for i in range(n):
        floor = i + 1
        result += floor * 100 * k + range_sum(k)

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
        input = """1 2"""
        output = """203"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3"""
        output = """1818"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
