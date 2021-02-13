# WA

import sys
from io import StringIO
import unittest
import copy
import sys

sys.setrecursionlimit(10**5)

takahashi_result = 0


def dfs(cur, d):
    # turn: true meands takahashi turn
    # return (x, y, c) x: ここに移動する人の取り分、y:移動しない人の取り分、c:ターン交代するか
    if cur not in d:
        return (0, 1, True)

    results = []
    for child in d[cur]:
        result = dfs(child, d)
        results.append(result)

    x = 0
    y = 1
    results_tmp = []
    results_tmp2 = []
    for result in results:
        if result[2] == False:
            if result[0] >= result[1]:
                x += result[0]
                y += result[1]
            else:
                results_tmp2.append(result)
        else:
            results_tmp.append(result)

    results_tmp.sort(key=lambda x: x[1]-x[0])
    for i in range(len(results_tmp)):
        result = results_tmp[i]
        if i % 2 == 0:
            x += result[0]
            y += result[1]
        else:
            y += result[0]
            x += result[1]

    c = len(results_tmp) % 2 == 0
    for i in range(len(results_tmp2)):
        result = results_tmp2[i]
        if c:
            y += result[0]
            x += result[1]
        else:
            x += result[0]
            y += result[1]

    # print("----------")
    # print(cur)
    # print((x, y, c))
    return (x, y, not c)


def resolve():
    n = int(input())
    P = list(map(int, input().split()))
    d = {}
    for i in range(n-1):
        p = P[i] - 1
        if p not in d:
            d[p] = []
        d[p].append(i+1)

    # print(d)
    print(dfs(0, d)[1])


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
        input = """10
1 2 3 4 5 6 7 8 9"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
1 1 3 1 3 6 7 6 6"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
