def main():
    n, t = list(map(int, input().split()))
    A = list(map(int, input().split()))
    
    total = sum(A)
    t = t % total
    
    index = 0
    for i in range(n):
        if A[i] < t:
            t -= A[i]
        else:
            index = i
            break
    
    print(index + 1, t)
    


if __name__ == '__main__':
    main()
