def solve():
    N, M = list(map(int, input().split()))
    number = [-1] * N
    for i in range(M):
        s, c = list(map(int, input().split()))
        s = s - 1
        if number[s] == -1 or number[s] == c:
            number[s] = c
        else:
            return -1

    if N != 1 and number[0] == 0:
        return -1

    if number[0] == -1:
        if N == 1:
            number[0] = 0
        else:
            number[0] = 1

    for i in range(1, N):
        if number[i] == -1:
            number[i] = 0

    return int(''.join(map(str, number)))


if __name__ == "__main__":
    print(solve())
