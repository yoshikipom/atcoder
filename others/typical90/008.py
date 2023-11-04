T = 'atcoder'
MOD = 10**9+7

def main():
    n = int(input())
    s = input()
    
    dp = [0 for _ in range(len(T)+1)]
    dp[0] = 1
    
    for i in range(n):
        c = s[i]
        for j in range(len(T)):
            if c == T[j]:
                dp[j+1] += dp[j]
                dp[j+1] %= MOD
        # print(*dp)
    
    print(dp[-1])


if __name__ == '__main__':
    main()
