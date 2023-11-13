import math

def main():
    n, l = list(map(int, input().split()))
    
    result = 0
    for i in range(0, n//l+1):
        a = i
        b = n-l*i
        result += math.comb(a+b, a)
        result %= 10**9+7
        # print(a,b)
        
    print(result)


if __name__ == '__main__':
    main()
            