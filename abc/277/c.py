def main():
    n = int(input())
    A = [None] * n
    B = [None] * n
    for i in range(n):
        A[i], B[i] = list(map(int, input().split()))

    d = {}
    d[1] = []
    for i in range(n):
        if A[i] not in d:
            d[A[i]] = []
        d[A[i]].append(B[i])

        if B[i] not in d:
            d[B[i]] = []
        d[B[i]].append(A[i])

    result = 1
    done = set()
    done.add(1)
    stack = [1]
    while stack:
        cur = stack.pop()
        result = max(result, cur)
        for next in d[cur]:
            if next not in done:
                done.add(next)
                stack.append(next)

    print(result)


if __name__ == '__main__':
    main()
