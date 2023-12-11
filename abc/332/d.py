import itertools


INF = float('inf')

def main():
    h, w = list(map(int, input().split()))
    A = []
    for _ in range(h):
        A.append(list(map(int, input().split())))
    B = []
    for _ in range(h):
        B.append(list(map(int, input().split())))
    
    P = list(itertools.permutations([i for i in range(h)]))
    Q = list(itertools.permutations([i for i in range(w)]))
    
    result = INF
    for p in P:
        for q in Q:
            cnt = 0
            
            # constcut a matrix
            X = [[None for _ in range(w)] for _ in range(h)]
            for i in range(h):
                ii = p[i]
                for j in range(w):
                    jj = q[j]
                    X[i][j] = A[ii][jj]
            
            # verify equality
            if not X == B:
                continue
            
            # cnt inversion number
            cnt = 0
            for i in range(h):
                for j in range(i+1,h):
                    if p[i] > p[j]:
                        cnt+=1

            for i in range(w):
                for j in range(i+1,w):
                    if q[i] > q[j]:
                        cnt+=1
            # print(p)
            # print(q)
            # print(cnt)
            
            # max
            result = min(result, cnt)
    
    if result == INF:
        print(-1)
        return
    
    print(result)            

if __name__ == '__main__':
    main()
