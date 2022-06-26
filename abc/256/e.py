
import sys
import unittest
from collections import defaultdict

def resolve():
    has_set = set()
    n = int(input())
    X = list(map(int, input().split()))
    X = list(map(lambda x:x-1, X))
    for x in X:
        has_set.add(x)
    C = list(map(int, input().split()))
    uf = UnionFind(n)
    for i in range(n):
        # print('i', i)
        if i in has_set:
            uf.union(i, X[i])

    result = 0
    for group_members in uf.all_group_members().values():
        # print(group_members)
        tmp = 10 ** 9 + 1
        if len(group_members) == 1:
            continue
        for member in group_members:
            tmp = min(tmp, C[member])
        result += tmp
    print(result)



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
2 3 2
1 10 100"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
7 3 5 5 8 4 1 2
36 49 73 38 30 85 27 45"""
        output = """57"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
