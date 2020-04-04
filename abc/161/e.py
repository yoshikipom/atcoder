if __name__ == "__main__":
    N, K, C = map(int, input().split())
    S = input()

    L = []
    i = 0
    while len(L) < K:
        if S[i] == 'o':
            L.append(i)
            i += C
        i += 1

    R = []
    i = N-1
    while len(R) < K:
        if S[i] == 'o':
            R.append(i)
            i -= C
        i -= 1
    R = R[::-1]

    # print(L)
    # print(R)

    for i in range(K):
        if L[i] == R[i]:
            print(L[i] + 1)
