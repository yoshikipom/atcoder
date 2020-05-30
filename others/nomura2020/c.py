def solve():
    N = int(input()) + 1
    A = list(map(int, input().split()))

    if N == 1:
        if A[0] == 1:
            return 1
        else:
            return -1

    # max node
    MN = [0 for _ in range(N)]
    MN[0] = 1
    for i in range(1, N):
        MN[i] = (MN[i-1] - A[i-1]) * 2
        if MN[i] <= 0:
            return -1

    if A[N-1] > MN[N-1]:
        return -1

    results = [0 for _ in range(N)]
    results[N-1] = A[N-1]
    if results[N-1] <= 0:
        return -1
    for i in range(N-2, -1, -1):
        results[i] += min(results[i+1] + A[i], MN[i])
        if results[i] <= 0:
            return -1

    return sum(results)

    # print(MI)
    # print(results)


if __name__ == "__main__":
    print(solve())
