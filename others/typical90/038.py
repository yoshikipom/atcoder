import math


def main():
    a, b = list(map(int, input().split()))
    gcd = math.gcd(a, b)
    
    result = a//gcd*b
    
    if result > 10**18:
        print('Large')
    else:
        print(result)


if __name__ == '__main__':
    main()
