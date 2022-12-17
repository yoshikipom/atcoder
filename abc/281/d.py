def main():
    n, k, d = list(map(int, input().split()))
    A = list(map(int, input().split()))
    dp = [[(-1, (1 << n) - 1) for j in range(d)] for i in range(k+1)]

    for i, a in enumerate(A):
        if a > dp[1][a % d][0]:
            dp[1][a % d] = (a, ((1 << n) - 1) & ~(1 << i))

    for i in range(2, k+1):
        for j in range(d):
            prev_val, prev_bit = dp[i-1][j]
            if prev_val == -1:
                continue
            for jj in range(n):
                if (prev_bit >> jj) & 1:
                    next_val = prev_val + A[jj]
                    next_val_index = next_val % d
                    # print(i, j, jj, next_val)
                    # if next_val % d == j and next_val > dp[i][(j+A[jj]) % d][0]:
                    if next_val > dp[i][next_val_index][0]:
                        # print('update')
                        dp[i][next_val_index] = (next_val, prev_bit & ~(1 << jj))

    # for row in dp:
    #     for item in row:
    #         print(item[0], bin(item[1])[2:].zfill(n), end=', ')
    #     print()

    if dp[-1][0][0] % d != 0:
        print(-1)
    else:
        print(dp[-1][0][0])


if __name__ == '__main__':
    main()
