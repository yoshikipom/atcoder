
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


didjs = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
]

def main():
    h, w = list(map(int, input().split()))
    M = [[False for _ in range(w)] for _ in range(h)]
    m = int(input())
    d ={}
    uf = UnionFind(m)
    for i in range(m):
        q = list(map(int, input().split()))
        if q[0] == 1:
            # add to map
            r, c = q[1], q[2]
            r-=1
            c-=1
            M[r][c] = True
            d[(r,c)] = i
            for di, dj in didjs:
                if not 0 <= r+di < h:
                    continue
                if not 0 <= c+dj < w:
                    continue
                if (r+di, c+dj) in d:
                    uf.union(d[(r+di, c+dj)], i)
            
        elif q[0] == 2:
            # output yes/no
            ra, ca, rb, cb = q[1:]
            ra-=1
            ca-=1
            rb-=1
            cb-=1
            if (ra,ca) not in d or (rb,cb) not in d:
                print('No')
                continue
            
            if uf.find(d[(ra,ca)]) == uf.find(d[(rb,cb)]):
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()
