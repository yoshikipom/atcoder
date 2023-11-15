def main():
    n, k = list(map(int, input().split()))
    
    tmp = 0
    for i, c in enumerate(str(n)[::-1]):
        tmp += int(c)*(8**i)
        
    # print(tmp)
    
    for _ in range(k):
        A = []
        while tmp > 0:
            A.append(str(tmp%9))
            tmp//=9
        for i, c in enumerate(A):
            if c == '8':
                A[i] = '5'
        for i, c in enumerate(A):
            tmp += int(c)*(8**i)
           
    A = []     
    while tmp > 0:
        A.append(str(tmp%8))
        tmp//=8
    if A:
        print(''.join(A[::-1]))
    else:
        print(0)


if __name__ == '__main__':
    main()
    