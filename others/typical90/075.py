import collections
import math

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return collections.Counter(a) # [(2, 3), (3, 1), (5, 1), (7, 1)]


def main():
    n = int(input())
    
    num = 0
    # print(prime_factorize(n))
    for prime, cnt in prime_factorize(n).items():
        num += cnt
        
    print(math.ceil(math.log2(num)))


if __name__ == '__main__':
    main()
