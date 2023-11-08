from collections import defaultdict


L = 1001

def main():
    n = int(input())
    A = [[0 for _ in range(L)] for _ in range(L)]
    B = [[0 for _ in range(L)] for _ in range(L)]
    
    for _ in range(n):
        lx, ly, rx, ry = list(map(int, input().split()))
        A[lx][ly] += 1
        A[rx][ly] -= 1
        A[lx][ry] -= 1
        A[rx][ry] += 1
        
    # for row in A:
    #     print(*row)
    # print()
    
    for x in range(L):
        total = 0
        for y in range(L):
            total += A[x][y]
            B[x][y] = total
            
    # for row in B:
    #     print(*row)
    
    for y in range(L):
        total = 0
        for x in range(L):
            total += B[x][y]
            B[x][y] = total
    
    # print()
    # for row in B:
    #     print(*row)
    
    d = defaultdict(int)
    for x in range(L):
        for y in range(L):
            d[B[x][y]]+=1

    for i in range(1,n+1):
        print(d[i])
    

if __name__ == '__main__':
    main()
