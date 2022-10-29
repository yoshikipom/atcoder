MOD = 998244353


def main():
    n, m, k = list(map(int, input().split()))

    dp = [[0 for j in range(n+1)] for i in range(k+1)]  # [ターン][どこにいるか] = 確率
    m_inv = pow(m, MOD-2, MOD)

    dp[0][0] = 1
    for i in range(k):
        for j in range(n):
            for a in range(1, m+1):
                # print(i,j,a)
                if j + a > n:
                    dp[i+1][2*n - j-a] += dp[i][j] * m_inv % MOD
                else:
                    dp[i+1][j+a] += dp[i][j] * m_inv % MOD
        dp[i+1][n] += dp[i][n]

    # print('debug')
    # for row in dp:
    #     print(*row)

    print(dp[-1][-1] % MOD)


if __name__ == '__main__':
    main()
