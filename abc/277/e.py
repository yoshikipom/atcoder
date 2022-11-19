from collections import deque
import queue


def main():
    n, m, k = list(map(int, input().split()))
    U = [None] * m
    V = [None] * m
    A = [None] * m
    for i in range(m):
        U[i], V[i], A[i] = list(map(int, input().split()))
    S = set(list(map(int, input().split())))

    routes_a = {}
    routes_b = {}
    for i in range(m):
        if A[i] == 0:
            if U[i] not in routes_a:
                routes_a[U[i]] = []
            routes_a[U[i]].append(V[i])
            if V[i] not in routes_a:
                routes_a[V[i]] = []
            routes_a[V[i]].append(U[i])
        else:
            if U[i] not in routes_b:
                routes_b[U[i]] = []
            routes_b[U[i]].append(V[i])
            if V[i] not in routes_b:
                routes_b[V[i]] = []
            routes_b[V[i]].append(U[i])
    
    min_dist_b = [None] * (n+1)
    min_dist_a = [None] * (n+1)
    q = deque()
    q.appendleft((1, 0, True))
    min_dist_a[1] = 0
    min_dist_b[1] = 0
    done_a = set()
    done_b = set()
    result = -1
    while q:
        # print(q)
        cur, cost, mode = q.pop()

        if cur == n:
            result = cost
            break

        if mode == True:
            routes = routes_b
            done = done_a
        else:
            routes = routes_a
            done = done_b
        done.add(cur)

        if cur in routes:
            for next in routes[cur]:
                if next not in done:
                    q.appendleft((next, cost+1, mode))

        if cur not in S:
            continue

        if mode == False:
            routes = routes_b
            done = done_a
        else:
            routes = routes_a
            done = done_b
        done.add(cur)

        if cur in routes:
            for next in routes[cur]:
                if next not in done:
                    q.appendleft((next, cost+1, not mode))


    print(result)


if __name__ == '__main__':
    main()
