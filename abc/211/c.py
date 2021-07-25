import sys
from io import StringIO
import unittest

T = 'chokudai'
MOD = 10**9 + 7


def resolve():
    S = input()
    # dp[i][j] Sのi文字目までみて、Tのj文字目の手前まで終わっている個数
    # dp = [[0 for i in range(8)]]
    dp = [0 for _ in range(9)]

    dp[0] = 1

    for i in range(len(S)):
        c = S[i]
        for j in range(len(T)):
            t = T[j]
            if c == t:
                dp[j+1] += dp[j]
                dp[j+1] %= MOD
        # print('i', i)
        # print(dp)

    print(dp[-1])


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
        input = """chchokudai"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoderrr"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """chokudaichokudaichokudai"""
        output = """45"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
