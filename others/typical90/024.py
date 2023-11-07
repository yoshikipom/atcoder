def main():
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    C = [None] * n
    for i in range(n):
        C[i] = B[i] - A[i]
        
    distance = 0
    for i in range(n):
        distance += abs(C[i])
        
    if distance > k or (k-distance) % 2 == 1:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
