if __name__ == "__main__":
    H, W = list(map(int, input().split()))
    A = []
    for _ in range(H):
        s = input()
        A.append(s)

    cost = [[float("inf") for i in range(W)] for i in range(H)]

    cost[0][0] = 1 if A[0][0] == '#' else 0

    for i in range(H)[1:]:
        if A[i-1][0] == '.' and A[i][0] == '#':
            cost[i][0] = cost[i-1][0] + 1
        else:
            cost[i][0] = cost[i-1][0]

    for j in range(W)[1:]:
        if A[0][j-1] == '.' and A[0][j] == '#':
            cost[0][j] = cost[0][j-1] + 1
        else:
            cost[0][j] = cost[0][j-1]

    for i in range(H)[1:]:
        for j in range(W)[1:]:

            # right
            if A[i][j-1] == '.' and A[i][j] == '#':
                cost_right = cost[i][j-1] + 1
            else:
                cost_right = cost[i][j-1]

            # down
            if A[i-1][j] == '.' and A[i][j] == '#':
                cost_down = cost[i-1][j] + 1
            else:
                cost_down = cost[i-1][j]

            cost[i][j] = min(cost_down, cost_right)

    # print(cost)
    print(cost[H-1][W-1])
