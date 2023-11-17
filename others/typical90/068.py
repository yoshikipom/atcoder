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


def main():
    n = int(input())
    q = int(input())
    T = [None] * q
    X = [None] * q
    Y = [None] * q
    V = [None] * q
    for i in range(q):
        T[i], X[i], Y[i], V[i] = list(map(int, input().split()))
        X[i] -= 1
        Y[i] -= 1
    
    R = [None] * (n-1) # R[i] is sum of A[i] + A[i+1]
    for i in range(q):
        if T[i] == 1:
            continue
        # t==0 のみ
        R[X[i]] = V[i]

    A = [None] * (n) # one expectation which meets all t==0 queries
    val = 0
    A[0] = 0
    for i in range(n-1):
        if R[i] == None:
            val = 0
        else:
            val = R[i] - val
        A[i+1] = val
    
    # print(A)
    
    # resolve
    uf = UnionFind(n)
    for i in range(q):
        if T[i] == 0:
            uf.union(X[i], Y[i])
        elif T[i] == 1:
            if not uf.same(X[i], Y[i]):
                print('Ambiguous')
                continue
            diff = V[i] - A[X[i]]
            is_plus_diff = (X[i]+Y[i])%2==0
            if is_plus_diff:
                goal = A[Y[i]] + diff
            else:
                goal = A[Y[i]] - diff
            print(goal)
        else:
            raise Exception('error')

if __name__ == '__main__':
    main()
