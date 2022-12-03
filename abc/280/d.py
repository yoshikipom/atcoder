from functools import lru_cache
import collections


@lru_cache(maxsize=None)
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
    return a

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def calc_required_base(k, count):
    # for i in range(1, 1000):
    #     tmp = (i * (i+1))//2
    #     if count <= tmp:
    #         return i
    tmp = 0
    for i in range(k, 10**12+1, k):
        # tmp += i // k
        pm = collections.Counter(prime_factorize(i))
        tmp += pm[k]
        # print('ik', i, k, tmp, count)
        if count <= tmp:
            return i
        

def main():
    # for i in range(1, 30):
    #     print(i, factorial(i))
    K = int(input())
    prime_map = collections.Counter(prime_factorize(K))
    
    result = 0
    for k, v in prime_map.items():
        # print(k, calc_required_base(k, v))
        result = max(calc_required_base(k, v), result)
        

    print(result)
    
if __name__ == '__main__':
    main()
