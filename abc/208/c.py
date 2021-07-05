import sys
from io import StringIO
import unittest


def resolve():
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))

    everyone = k // n
    rest = k % n

    B = []
    for i in range(n):
        B.append((i, A[i]))

    winner = set()
    B.sort(key=lambda x: x[1])
    for i in range(rest):
        winner.add(B[i][0])

    # print(everyone)
    # print(rest)
    # print(winner)

    for i in range(n):
        if i in winner:
            print(everyone+1)
        else:
            print(everyone)


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
        input = """2 7
1 8"""
        output = """4
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 3
33"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 1000000000000
99 8 2 4 43 5 3"""
        output = """142857142857
142857142857
142857142858
142857142857
142857142857
142857142857
142857142857"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
