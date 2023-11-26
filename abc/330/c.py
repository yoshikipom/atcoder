import math


def main():
    D = int(input())
    
    result = float('inf')
    for x in range(2*10**6):
        y1 = math.floor(pow(abs(D - x**2), 1/2))
        y2 = y1 + 1
        result = min(result, abs(x**2+y1**2-D))
        result = min(result, abs(x**2+y2**2-D))
        
    print(result)


if __name__ == '__main__':
    main()
