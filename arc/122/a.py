import sys
from io import StringIO
import unittest
MOD = 10**9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    dp = [[0 for j in range(4)] for i in range(n)]
    dp[0][0] = 1
    dp[0][1] = 0
    dp[0][2] = A[0]
    dp[0][3] = 0

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][0] %= MOD
        dp[i][1] = dp[i-1][0]
        dp[i][1] %= MOD
        dp[i][2] = dp[i-1][2] + A[i] * dp[i-1][0] + \
            dp[i-1][3] + A[i] * dp[i-1][1]
        dp[i][2] %= MOD
        dp[i][3] = dp[i-1][2] - A[i] * dp[i-1][0]
        dp[i][3] %= MOD
        # print('-------------------')
        # print(dp[i-1][2] + A[i] * dp[i-1][0])
        # print(dp[i-1][3] + A[i] * dp[i-1][1])
        # print(dp[i-1][2] - A[i] * dp[i-1][0])

    # for row in dp:
        # print(*row)

    # pattern = dp[-1][0] + dp[-1][1]

    result = (dp[-1][2] + dp[-1][3]) % MOD
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
3 1 5"""
        output = """15"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
866111664 178537096 844917655 218662351 383133839 231371336 353498483 865935868 472381277 579910117"""
        output = """279919144"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
