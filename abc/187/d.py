import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    AB = []
    B = []
    sum_a = 0
    sum_b = 0
    for _ in range(n):
        a, b = list(map(int, input().split()))
        AB.append((a, b))
        sum_a += a
        sum_b += b
    aoki = sum_a
    takahashi = 0

    AB.sort(key=lambda x: 2 * x[0] + x[1], reverse=True)
    # print(AB)
    result = 0
    for a, b in AB:
        result += 1
        aoki -= a
        takahashi += a + b
        if aoki < takahashi:
            break

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
        input = """4
2 1
2 2
5 1
1 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2 1
2 1
2 1
2 1
2 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
273 691"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
