if __name__ == "__main__":
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    # print(A)

    min_d = 1000000
    for i in range(1, N):
        d = K - (A[i] - A[i-1])
        min_d = min(min_d, d)

    d = A[N-1] - A[0]
    min_d = min(min_d, d)

    print(min_d)
