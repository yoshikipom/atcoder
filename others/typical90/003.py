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
    
    seen = set()
    max_length = 0
    seen.add(1)
    
    
    def dfs(cur, depth) -> int:
        nonlocal max_length
        branch_depth_max = depth
        for next_cur in d[cur]:
            if next_cur in seen:
                continue
            seen.add(next_cur)
            branch_depth = dfs(next_cur, depth+1)
            max_length = max(max_length, branch_depth_max-depth+branch_depth-depth)
            branch_depth_max = max(branch_depth_max, branch_depth)
        # print("debug", cur, branch_depth_max)
        return branch_depth_max
    
    dfs(1, 0)
    
    print(max_length+1)


if __name__ == '__main__':
    main()
