import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    divs = [0 for i in range(200)]

    for a in A:
        divs[a % 200] += 1

    result = 0
    for div in divs:
        if div >= 2:
            result += div * (div-1) // 2

    # print(*divs)
    print(int(result))


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
        input = """6
123 223 123 523 200 2000"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2 3 4 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
199 100 200 400 300 500 600 200"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
