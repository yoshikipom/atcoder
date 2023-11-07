import math

def main():
    a, b, c = list(map(int, input().split()))
    
    gcd = math.gcd(a, b)
    gcd = math.gcd(gcd, c)
    
    # print(gcd)
    
    result = (a+b+c)//gcd-3
    
    print(result)


if __name__ == '__main__':
    main()
