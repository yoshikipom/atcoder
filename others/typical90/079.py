def main():
    h, w = list(map(int, input().split()))
    A = []
    for _ in range(h):
        A.append(list(map(int, input().split())))
    B = []
    for _ in range(h):
        B.append(list(map(int, input().split())))
    C = [[None for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            C[i][j] = A[i][j]- B[i][j]
    
    # print('=====')
    # for row in C:
    #     print(*row)
    
    result = 0
    for i in range(h-1):
        for j in range(w-1):
            if C[i][j] == 0:
                continue
            tmp = C[i][j]
            result += abs(tmp)
            for di in range(2):
                for dj in range(2):
                    C[i+di][j+dj] -= tmp
                    
    for i in range(h):
        for j in range(w):
            if C[i][j] != 0:
                print('No')
                return
    
    # print('=====')
    # for row in C:
    #     print(*row)
    
    print('Yes')
    print(result)

if __name__ == '__main__':
    main()
