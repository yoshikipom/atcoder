import sys
from io import StringIO
import unittest


def resolve():
    k, n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))

    B = []
    AA = []
    BB = []
    for i, a in enumerate(A):
        b = m * a / n
        B.append(int(b))
        BB.append((abs(int(b)*n - a*m), i))
        AA.append(a/n)

    BB.sort(key=lambda x: x[0], reverse=True)

    s = m-sum(B)
    for i in range(s):
        B[BB[i][1]] += 1

    # print(sum(B), m, m-sum(B))
    print(*B)
    # print(*BB)


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
        input = """3 7 20
1 2 4"""
        output = """3 6 11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3 100
1 1 1"""
        output = """34 33 33"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 10006 10
10000 3 2 1 0 0"""
        output = """10 0 0 0 0 0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 78314 1000
53515 10620 7271 3817 1910 956 225"""
        output = """683 136 93 49 24 12 3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
