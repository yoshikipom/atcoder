import sys
from io import StringIO
import unittest
import copy
import bisect


def solve(n, m, WV, X):
    result = 0
    X.sort()
    # print('------solve------')
    for w, v in WV:
        # print(v, w, "X:", X, "result: ", result)

        index = bisect.bisect_left(X, w)
        if index == len(X):
            continue
        result += v
        del X[index]
    print(result)


def resolve():
    n, m, q = list(map(int, input().split()))
    WV = []
    for _ in range(n):
        w, v = list(map(int, input().split()))
        WV.append((w, v))

    WV.sort(key=lambda x: x[1], reverse=True)
    X = list(map(int, input().split()))

    for _ in range(q):
        l, r = list(map(int, input().split()))
        X_alt = copy.copy(X)
        del X_alt[l-1: r]
        solve(n, m, WV, X_alt)


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
        input = """3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3"""
        output = """20
0
9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
