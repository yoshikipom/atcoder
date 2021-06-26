import sys
from io import StringIO
import unittest
import math

from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    A1 = A[:n//2]
    A2 = A[math.ceil(n/2):]
    A2.reverse()

    s = set()
    for i in range(n//2):
        if A1[i] == A2[i]:
            continue
        l = [A1[i], A2[i]]
        l.sort()
        s.add(tuple(l))

    uf = UnionFind(2 * 10 ** 5 + 1)

    for a, b in s:
        uf.union(a, b)

    count = 0
    for root in uf.roots():
        count += uf.size(root) - 1

    print(count)

    # print(A1)
    # print(A2)
    # print(s)
    # print(s2)


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
        input = """8
1 5 3 2 5 2 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
1 2 3 4 1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
200000"""
        output = """0"""
        self.assertIO(input, output)
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
1 2 3 4 5 6"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
