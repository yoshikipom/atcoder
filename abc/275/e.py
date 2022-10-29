MOD = 998244353

def main():
    n, m, k = list(map(int, input().split()))

    dp = [[0 for j in range(n+1)] for i in range(k+1)]  # [ターン][どこにいるか] = case数

    dp[0][0] = 1
    for i in range(k):
        for j in range(n):
            for a in range(1, m+1):
                # print(i,j,a)
                if j + a > n:
                    dp[i+1][2*n - j-a] += dp[i][j]
                else:
                    dp[i+1][j+a] += dp[i][j]
        # dp[i+1][n] += dp[i][n]
    
    print('debug')
    for row in dp:
        print(*row)

    numerator = dp[-1][-1] % MOD
    denominator = sum(dp[-1])
    # print(numerator, denominator)
    result = (numerator * pow(denominator, MOD-2, MOD)) % MOD
    print(result)

    numerator = 0
    denominator = 0
    result = 0
    for i in range(1, k+1):
        numerator += dp[i][-1] % MOD
        denominator += sum(dp[i]) % MOD
        result += numerator * pow(denominator, MOD-2, MOD) % MOD
        print(i)
        print(dp[i][-1], sum(dp[i]))
        print(result)
    # print(numerator, denominator)
    print(result)



if __name__ == '__main__':
    main()
