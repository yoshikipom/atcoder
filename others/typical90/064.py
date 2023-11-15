import itertools


def main():
    n, q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    D = []
    for i in range(n-1):
        D.append(A[i+1]-A[i])

    result = 0    
    for d in D:
        result += abs(d)
    # print(D)

    for _ in range(q):
        l, r, v = list(map(int, input().split()))
        l-=1
        r-=1
        if l == 0:
            l_change = 0
        else:
            l_change = abs(D[l-1]+v)-abs(D[l-1])
            D[l-1] += v
            
        if r == n-1:
            r_change = 0
        else:
            r_change = abs(D[r]-v)-abs(D[r])
            D[r] -= v
        result += l_change + r_change
            
        # print(D)
        # print('debug:', l_change, r_change, D)
        print(result)

if __name__ == '__main__':
    main()
