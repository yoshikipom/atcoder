def main():
    n, s = list(map(int, input().split()))
    A = [0]
    B = [0]
    for i in range(n):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
        
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    
    for i in range(n+1):
        a = A[i]
        b = B[i]
        for j in range(s+1):
            if j >= a and dp[i-1][j-a] == True:
                dp[i][j] = True
                continue
            if j >= b and dp[i-1][j-b] == True:
                dp[i][j] = True
                continue
    
    if dp[-1][-1] == False:
        print('Impossible')
        return
        
    route = []
    cur = s
    for i in range(1,n+1)[::-1]:
        # print(route)
        if cur-A[i]>=0 and dp[i-1][cur-A[i]] == True:
            route.append('A')
            cur -= A[i]
        elif cur-B[i]>=0 and dp[i-1][cur-B[i]] == True:
            route.append('B')
            cur -= B[i]
        else:
            raise Exception('invalid route')
        
    print(''.join(route[::-1]))

if __name__ == '__main__':
    main()
