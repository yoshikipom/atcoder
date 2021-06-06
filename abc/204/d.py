import math
import bisect
import sys
from io import StringIO
import unittest
import sys
sys.setrecursionlimit(10000)


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    m = n * 1000 + 1

    dp = [False for i in range(m)]
    dp[0] = True

    for i in range(n):
        a = A[i]
        for j in reversed(range(m)):
            if j - a >= 0 and dp[j - a] == True:
                dp[j] = True

    L = []
    for i in range(m):
        if dp[i]:
            L.append(i)

    # def dfs(i, value, S):
    #     S.add(value)

    #     if i >= n:
    #         return

    #     dfs(i+1, value + A[i], S)
    #     dfs(i+1, value, S)

    # S = set()
    # dfs(0, 0, S)

    # L = list(S)

    L.sort()

    # print(L)

    index = bisect.bisect_left(L, math.ceil(sum(A)/2))

    print(L[index % m])


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
        input = """5
8 3 7 2 5"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1000 1"""
        output = """1000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9
3 14 15 9 26 5 35 89 79"""
        output = """138"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
