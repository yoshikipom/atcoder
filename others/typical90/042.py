MOD = 10**9 + 7


def main():
    k = int(input())
    
    if k % 9 != 0:
        print(0)
        return
    else:
        dp = [0] * (k+1) # dp[i] は 合計がiになる組み合わせ数。
        dp[0] = 1
        for i in range(k+1):
            digit = min(i, 9)
            for j in range(1, digit+1):
                dp[i] += dp[i-j] # 集めるDP。合計がiになる組み合わせ数
                dp[i] %= MOD
        print(dp[k])    
        


if __name__ == '__main__':
    main()
