import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    S = []
    for _ in range(n):
        s = input()
        S.append(s)

    dp = [[0 for j in range(2)] for i in range(n+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, n+1):
        if S[i-1] == 'AND':
            dp[i][0] = dp[i-1][0] * 2 + dp[i-1][1]  # x: true/false, false
            dp[i][1] = dp[i-1][1]  # x: true
        else:
            dp[i][0] = dp[i-1][0]  # x: false
            dp[i][1] = dp[i-1][0] + dp[i-1][1] * 2  # x: true, true/false
    print(dp[-1][1])
    # for row in dp:
    #     print(*row)


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
        input = """2
AND
OR"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
OR
OR
OR
OR
OR"""
        output = """63"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
