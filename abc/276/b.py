def main():
    n, m = list(map(int, input().split()))
    A = [None for i in range(m)]
    B = [None for i in range(m)]
    for i in range(m):
        A[i], B[i] = list(map(int, input().split()))

    d = {}
    for i in range(1, n+1):
        d[i] = []

    for i in range(m):
        d[A[i]].append(B[i])
        d[B[i]].append(A[i])

    for i in range(1, n+1):
        values = d[i]
        values = list(set(values))
        values.sort()
        values = [str(i) for i in values]
        print(len(values), " ".join(values))

    # print(d)


if __name__ == '__main__':
    main()
