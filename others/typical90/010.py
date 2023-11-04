def main():
    n = int(input())
    S_1 = [0] * (n+1)
    S_2 = [0] * (n+1)

    for i in range(n):
        c, p = list(map(int, input().split()))
        if c == 1:
            S_1[i+1] = p
        elif c == 2:
            S_2[i+1] = p
        else:
            raise Exception("error")
        
    q = int(input())
    L = []
    R = []
    for i in range(q):
        l, r = list(map(int, input().split()))
        L.append(l)
        R.append(r)
    
    A_1 = [0] * (n+1)
    A_2 = [0] * (n+1)
    for i in range(1,n+1):
        A_1[i] = A_1[i-1] + S_1[i]
        A_2[i] = A_2[i-1] + S_2[i]
    
    # print(A_1)
    # print(A_2)
    
    for i in range(q):
        l = L[i]
        r = R[i]
        print(A_1[r]-A_1[l-1], A_2[r]-A_2[l-1])
            

if __name__ == '__main__':
    main()
