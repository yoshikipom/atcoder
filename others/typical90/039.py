from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    d = defaultdict(list)
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        d[a].append(b)
        d[b].append(a)

    dp = [0 for _ in range(n+1)] # dp[i]: node i 以下のnode数
    
    seen = set()
    def dfs(cur):
        dp[cur] = 1
        for next_cur in d[cur]:
            if next_cur in seen:
                continue
            seen.add(next_cur)
            dfs(next_cur)
            dp[cur] += dp[next_cur]

    seen.add(1)
    dfs(1)
    
    result = 0
    seen = set()
    def dfs2(cur):
        nonlocal result
        for next_cur in d[cur]:
            if next_cur in seen:
                continue
            seen.add(next_cur)
            dfs2(next_cur)
            result += dp[next_cur] * (n-dp[next_cur])
    
    seen.add(1)
    dfs2(1)
    
    print(result)

if __name__ == '__main__':
    main()
