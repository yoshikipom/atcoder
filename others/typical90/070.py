def main():
    n = int(input())
    X = [None] * n
    Y = [None] * n
    for i in range(n):
        X[i], Y[i] = list(map(int, input().split()))
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    if n % 2 == 0:
        x = (X_sorted[n//2] + X_sorted[n//2-1]) / 2.0
        y = (Y_sorted[n//2] + Y_sorted[n//2-1]) / 2.0
    else:
        x = X_sorted[n//2]
        y = Y_sorted[n//2]
        
    # print('x, y= ', x, y)
    
    result = 0
    for i in range(n):
        result += abs(X[i]-x) + abs(Y[i]-y)
        
    print(int(result))

if __name__ == '__main__':
    main()
