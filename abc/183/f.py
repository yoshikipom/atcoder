from collections import defaultdict


class UnionFind():
    def __init__(self, n, C):
        self.n = n
        self.parents = [-1] * n
        self.m = [{} for i in range(n)]
        for i in range(n):
            if C[i] not in self.m[i]:
                self.m[i][C[i]] = 0
            self.m[i][C[i]] += 1

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
        for k, v in self.m[y].items():
            if k not in self.m[x]:
                self.m[x][k] = 0
            self.m[x][k] += v

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
        return '\n'.join('{r}: {m}' for r, m in self.all_group_members().items())


if __name__ == "__main__":
    n, q = list(map(int, input().split()))
    C = list(map(int, input().split()))
    uf = UnionFind(n, C)
    for _ in range(q):
        op, a, b = list(map(int, input().split()))

        if op == 1:
            a -= 1
            b -= 1
            uf.union(a, b)
        else:
            a -= 1
            index = uf.find(a)
            if b not in uf.m[index]:
                print(0)
            else:
                print(uf.m[index][b])
