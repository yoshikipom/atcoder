from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**7)

def main():
    n, m = list(map(int, input().split()))
    d = defaultdict(list)
    d2 = defaultdict(list)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        a-=1
        b-=1
        d[a].append(b)
        d2[b].append(a)
    
    seen = set()
    index = 0
    order = [None] * n
    
    def dfs(cur):
        nonlocal index
        
        if cur in seen:
            return
        seen.add(cur)
        
        for next_cur in d[cur]:
            if next_cur in seen:
                continue
            dfs(next_cur)
            
        order[n-1-index] = cur
        index+=1
        
    for start in range(n):
        dfs(start)
        
    # print(order)
    
    graphs = []
    seen = set()
    graph = []
    def dfs_for_graph(cur):
        if cur in seen:
            return
        seen.add(cur)
        graph.append(cur)
        
        for next_cur in d2[cur]:
            if next_cur in seen:
                continue
            dfs_for_graph(next_cur)
    
    for start in order:
        graph = []
        dfs_for_graph(start)
        if graph:
            graphs.append(graph)
    
    result = 0
    for graph in graphs:
        result += math.comb(len(graph), 2)
        
    print(result)

if __name__ == '__main__':
    main()
