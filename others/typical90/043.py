from collections import deque

INF = 10**6

dirs = (
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
)

def main():
    h, w = list(map(int, input().split()))
    rs, cs = list(map(int, input().split()))
    rt, ct = list(map(int, input().split()))
    rs -= 1
    cs -= 1
    rt -= 1
    ct -= 1
    M = []
    for _ in range(h):
        M.append(input())
        
    dist = [[[INF for _ in range(4)] for _ in range(w)] for _ in range(h)]
    q = deque()
    
    for i in range(4):
        dist[rs][cs][i] = 0
        q.appendleft((rs, cs, 0, i))
        
    
    while q:
        # print(q)
        
        # 現在の座標、コスト、向き
        r, c, cost, dir_index = q.pop()
        if dist[r][c][dir_index] < cost:
            continue
        
        # 4方向に進める。進んだ先のdistを埋める
        for i, dir in enumerate(dirs):
            dr, dc = dir
            if not 0 <= r+dr < h or not 0 <= c+dc < w:
                continue
            if M[r+dr][c+dc] == '#':
                continue
            
            if dir_index == i:
                # same direction
                if dist[r+dr][c+dc][i] > cost:
                    dist[r+dr][c+dc][i] = cost
                    q.append((r+dr, c+dc, cost, i))
            else:
                # other direction
                if dist[r+dr][c+dc][i] > cost+1:
                    dist[r+dr][c+dc][i] = cost+1
                    q.appendleft((r+dr, c+dc, cost+1, i))
    
    print(min(dist[rt][ct]))
        
    
if __name__ == '__main__':
    main()
