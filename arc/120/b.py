import sys
from io import StringIO
import unittest


MOD = 998244353


def resolve():
    h, w = list(map(int, input().split()))
    M = []
    for _ in range(h):
        row = input()
        M.append(row)

    # L = max(h, w)

    result = 1
    D = []

    for k in range(h + w - 1):
        # print('k=', k, 'l_max=', min(k+1, 2 * L-k-1))
        # print('k=', k)
        row = []
        l = k
        while l >= 0:
            i = l
            j = k - l

            if i >= h or j >= w:
                l -= 1
                continue

            row.append(M[i][j])

            # 全部.のとき
            # どっちかはあるとき
            # print(i, j)

            l -= 1

        D.append(row)

        r_count = row.count('R')
        b_count = row.count('B')
        free_count = row.count('.')

        if r_count != 0 and b_count != 0:
            print(0)
            return
        elif r_count == 0 and b_count == 0:
            result *= 2
            result %= MOD

    print(result)

    # for row in D:
    # print(*row)


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
        input = """2 2
B.
.R"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
R.R
BBR
..."""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2
BB
BB"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
