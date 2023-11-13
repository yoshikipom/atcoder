import bisect
from collections import defaultdict


INF = 3 * 10**5 + 1

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    R = list(reversed(A))
    R = [0] + R
    
    dp = [INF for i in range(n+1)]
    dp[0] = 0
    memo1 = {}
    
    cnt = 0
    for i in range(1, n+1):
        a = A[i]
        index = bisect.bisect_left(dp, a)
        dp[index] = min(dp[index], a)
        cnt = max(cnt, index)
        memo1[i] = cnt
    # print(dp)
    
    dp = [INF for i in range(n+1)]
    dp[0] = 0
    memo2 = {}
    
    cnt = 0
    for i in range(1, n+1):
        a = R[i]
        index = bisect.bisect_left(dp, a)
        dp[index] = min(dp[index], a)
        cnt = max(cnt, index)
        memo2[i] = cnt
        
    result = 0
    for index, c1 in memo1.items():
        tmp = n - index + 1
        c2 = memo2[tmp]
        result = max(result, c1 + c2 - 1)
        
        
    # print(memo1)
    # print(memo2)
    print(result)
    

if __name__ == '__main__':
    main()
