def main():
    n, k = list(map(int, input().split()))
    A = [0 for _ in range(n+1)] 
    for i in range(2, n+1):
        if A[i] != 0:
            continue
        for j in range(i, n+1, i):
            A[j] += 1
    
    
    c = 0
    for i in range(2, n+1):
        if A[i] >= k:
            c+= 1
    print(c)
    
if __name__ == '__main__':
    main()
