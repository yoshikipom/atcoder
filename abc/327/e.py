INF = 10**9

def main():
    n = int(input())
    P = list(map(int, input().split()))
    
    dp = [[-INF for _ in range(n+1)] for _ in range(n)]
    dp[0][1] = P[0]
    for i in range(n):
        dp[i][0]=0
    for i in range(1,n):
        p = P[i]
        for j in range(1,i+2):
            r=0.9*dp[i-1][j-1]+p
            dp[i][j] = max(dp[i-1][j], r)
        
        
    # for row in dp:
    #     print(*row)
        
    result = -INF
    for cnt in range(1,n+1):
        x = dp[-1][cnt]
        y = 1
        for j in range(1,cnt):
            y = y*0.9+1
        z = 1200/(cnt**(1/2))  
        result = max(result, x/y-z)
        # print(cnt, x/y-z, x, y, z)
        
    print(result)


if __name__ == '__main__':
    main()
