def main():
    h, w = list(map(int, input().split()))
    A = []
    for _ in range(h):
        A.append(list(map(int, input().split())))

    B = [[0 for _ in range(w)] for _ in range(h)]
    
    for i in range(h):
        s = 0
        for j in range(w):
            s += A[i][j]
        for j in range(w):
            B[i][j] += s
    
    for j in range(w):
        s = 0
        for i in range(h):
            s += A[i][j]
        for i in range(h):
            B[i][j] += s
            
    for i in range(h):
        for j in range(w):
            B[i][j] -= A[i][j]
    
    for row in B:
        print(*row)

if __name__ == '__main__':
    main()
