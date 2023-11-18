def main():
    n, k = list(map(int, input().split()))
    A = [None] * n
    B = [None] * n
    for i in range(n):
        A[i], B[i] = list(map(int, input().split()))
        
    h = max(A)+1
    w = max(B)+1
    M = [[0 for _ in range(w)]for _ in range(h)]
    for i in range(n):
        M[A[i]][B[i]] += 1

    M2 = [[0 for _ in range(w)]for _ in range(h)]
    for i in range(h):
        total_in_row = 0
        for j in range(w):
            total_in_row += M[i][j]
            M2[i][j] = total_in_row
    for j in range(w):
        total_in_column = 0
        for i in range(h):
            total_in_column += M2[i][j]
            M2[i][j] = total_in_column
            
    # print('M1======')
    # s = 0
    # for row in M:
    #     s+=sum(row)
    # print('s', s, h, w)
    # print('M2======')
    # for row in M2:
    #     print(*row)
    
    result = 0
    for i in range(1, h):
        for j in range(1, w):
            ii = min(i+k, h-1)
            jj = min(j+k, w-1)
            total = M2[ii][jj]-M2[i-1][jj]-M2[ii][j-1]+M2[i-1][j-1]
            result = max(result, total)
            
    print(result)

if __name__ == '__main__':
    main()
