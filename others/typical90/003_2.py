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
    max_depth = 0
    farest_node = 1
    seen.add(1)
    
    def dfs(cur, depth) -> int:
        nonlocal max_depth, farest_node
        if depth >= max_depth:
            max_depth = depth
            farest_node = cur
            
        for next_cur in d[cur]:
            if next_cur in seen:
                continue
            seen.add(next_cur)
            dfs(next_cur, depth+1)
        # print("debug", cur, branch_depth_max)
        return 
    
    dfs(1, 0)
    # print('debug', max_depth, farest_node)
    max_depth=0
    seen = set()
    dfs(farest_node, 0)
    
    print(max_depth+1)


if __name__ == '__main__':
    main()
