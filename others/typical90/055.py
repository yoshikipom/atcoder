import itertools
import math

def main():
    n,p,q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    for i in range(n):
        A[i] %= p
    result = 0
    for comb in itertools.combinations(A, 5):
        tmp = 1
        for num in comb:
            tmp *= num
            tmp %= p
        if tmp == q:
            result += 1
            
    print(result)



if __name__ == '__main__':
    main()
