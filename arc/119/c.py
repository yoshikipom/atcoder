import sys
from io import StringIO
import unittest
import itertools


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    for i in range(n):
        if i % 2 == 1:
            A[i] *= -1

    # print(A)
    accum = [0] + list(itertools.accumulate(A))
    # print(accum)

    # result = 0
    # for l in range(n):
    #     for r in range(l+1, n):
    #         if accum[r+1] - accum[l] == 0:
    #             print(l, r)
    #             result += 1

    # print(result)

    d = {}
    for a in accum:
        if a not in d:
            d[a] = 0
        d[a] += 1

    result = 0
    for k, v in d.items():
        if v <= 1:
            continue
        result += v * (v-1) // 2

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
        input = """5
5 8 8 6 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
12 8 11 3 3 13 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
8 6 3 9 5 4 7 2 1 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """14
630551244 683685976 249199599 863395255 667330388 617766025 564631293 614195656 944865979 277535591 390222868 527065404 136842536 971731491"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
