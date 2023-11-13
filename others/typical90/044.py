def main():
    n, q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    l = 0
    for _ in range(q):
        t, x, y = list(map(int, input().split()))
        x-=1
        y-=1
        if t==1:
            A[x-l], A[y-l] = A[y-l], A[x-l]
        elif t==2:
            l = (l+1)%n
        elif t==3:
            print(A[x-l])

        
if __name__ == '__main__':
    main()
