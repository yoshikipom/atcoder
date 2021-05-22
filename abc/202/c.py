import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = []
    for j in range(n):
        D.append(B[C[j]-1])

    d = {}
    for i in range(n):
        if A[i] not in d:
            d[A[i]] = 0
        d[A[i]] += 1

    result = 0

    for j in range(n):
        if D[j] in d:
            result += d[D[j]]

    # print(A)
    # print(D)
    # print(d)
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
        input = """3
1 2 2
3 1 2
2 3 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1
1 1 1 1
1 2 3 4"""
        output = """16"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
2 3 3
1 3 3
1 1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
