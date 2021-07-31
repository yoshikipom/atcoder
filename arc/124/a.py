import sys
from io import StringIO
import unittest

MOD = 998244353


def resolve():
    N, K = list(map(int, input().split()))

    A = [set() for _ in range(N)]
    tmp = [i for i in range(K)]
    for i in range(N):
        A[i] = set(tmp)

    fix = set()

    CK = []
    for index in range(K):
        c, k = input().split()
        k = int(k) - 1
        fix.add(k)
        if c == 'L':
            for i in range(N)[:k]:
                A[i].remove(index)
        else:
            for i in range(N)[k:]:
                A[i].remove(index)

    result = 1
    for i in range(N):
        if i in fix:
            continue
        result *= len(A[i])
        result %= MOD

    print(result)

    # print('fix', fix)
    # for i in range(N):
    #     print(i, A[i])


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
        input = """3 2
L 1
R 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """30 10
R 6
R 8
R 7
R 25
L 26
L 13
R 14
L 11
L 23
R 30"""
        output = """343921442"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
