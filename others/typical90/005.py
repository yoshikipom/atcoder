# 課題1のみ達成

MOD = 10 ** 9 + 7

def main():
    n, b, k = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    dp = [[0 for _ in range(b)] for _ in range(n)]
    
    for c in C:
        dp[0][c%b] += 1
    
    for i in range(n-1):
        for j in range(b):
            tmp = j*10
            for c in C:
                dp[i+1][(tmp+c)%b] += dp[i][j]
                dp[i+1][(tmp+c)%b] %= MOD
    
    # for row in dp:
    #     print(*row)
    
    print(dp[-1][0])


if __name__ == '__main__':
    main()
