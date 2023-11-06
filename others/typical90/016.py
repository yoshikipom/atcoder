def main():
    n = int(input())
    a,b,c = list(map(int, input().split()))
    
    result = float('inf')
    for i in range(10000):
        for j in range(10000-i):
            total = i*a + j*b
            if total > n:
                continue
            remain = n - total
            if remain%c!=0:
                continue
            # print(i,j,remain//c)
            result = min(result, i+j+remain//c)
    print(result)
    


if __name__ == '__main__':
    main()
