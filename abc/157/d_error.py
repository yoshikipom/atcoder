def dfs(F, seen, v):
    seen[v] = True

    for e in F[v]:
        if seen[e]:
            continue
        dfs(F, seen, e)


def solve():
    N, M, K = list(map(int, input(). split()))
    F = [[] for i in range(N)]
    Connections = []
    for i in range(M):
        c = [int(x) - 1 for x in input().split()]
        F[c[0]].append(c[1])
        F[c[1]].append(c[0])
        Connections.append(c)
    B = [[] for i in range(N)]
    for i in range(K):
        b = [int(x)-1 for x in input().split()]
        B[b[0]].append(b[1])
        B[b[1]].append(b[0])

    result = []
    for i in range(N):
        candidates = set([x for x in range(
            N) if x not in F[i] and x not in B[i] and x != i])
        seen = [False] * (N)
        for v in F[i]:
            dfs(F, seen, v)

        want = [candidate for candidate in candidates if seen[candidate]]
        result.append(str(len(want)))

    print(' '.join(result))


if __name__ == "__main__":
    solve()
