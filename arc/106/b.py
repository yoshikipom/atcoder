# https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n, A, B):
        self.n = n
        self.A = A
        self.B = B
        self.parents = [[-1, A[i], B[i]] for i in range(n)]

    def find(self, x):
        if self.parents[x][0] < 0:
            return x
        else:
            self.parents[x][0] = self.find(self.parents[x][0])
            return self.parents[x][0]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x][0] > self.parents[y][0]:
            x, y = y, x

        self.parents[x][0] += self.parents[y][0]
        self.parents[x][1] += self.parents[y][1]
        self.parents[x][2] += self.parents[y][2]
        self.parents[y][0] = x

    def size(self, x):
        return -self.parents[self.find(x)][0]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x[0] < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    uf = UnionFind(n, A, B)
    for _ in range(m):
        c, d = list(map(int, input().split()))
        c -= 1
        d -= 1
        uf.union(c, d)

    # print(uf.roots())
    # print(uf.group_count())
    can = True
    # for root, menbers in uf.all_group_members().items():
    #     # print(root, menbers)
    #     a_sum = sum(map(lambda index: A[index], menbers))
    #     b_sum = sum(map(lambda index: B[index], menbers))
    #     print(a_sum)
    #     if a_sum != b_sum:
    #         can = False
    #         break
    for root in uf.roots():
        if uf.parents[root][1] != uf.parents[root][2]:
            can = False
            break

    if can:
        print('Yes')
    else:
        print('No')
