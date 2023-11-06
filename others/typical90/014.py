def main():
    n = int(input())    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    
    result = 0
    for i in range(n):
        result += abs(A[i] - B[i])
    print(result)
        


if __name__ == '__main__':
    main()
