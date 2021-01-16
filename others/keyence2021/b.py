import sys
from io import StringIO
import unittest
import collections


def resolve():
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    d = collections.OrderedDict()
    A.sort()
    for a in A:
        if a not in d:
            d[a] = 0
        d[a] += 1
    max_a = max(A)
    for i in range(max_a+2):
        if i not in d:
            d[i] = 0
    # print(d)

    result = 0
    live = k
    for i in range(max_a+2):
        # print('i', i, 'live', live)
        count_i = d[i]
        if live <= count_i:
            # print('all live')
            continue
        else:
            # print('some die')
            die = live - count_i
            live = count_i
            result += die * i
    # if live > 0:
    #     result += live * (max_a+1)

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
        input = """4 2
0 1 0 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
0 1 1 2 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 4
6 2 6 8 4 5 5 8 4 1 7 8 0 3 6 1 1 8 3 0"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
