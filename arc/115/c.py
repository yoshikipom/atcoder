import sys
from io import StringIO
import unittest

import math


# def get_sieve_of_eratosthenes(n):
#     N = n
#     A = list(range(2, N+1))
#     p = list()
#     while A[0]**2 <= N:
#         tmp = A[0]
#         p.append(tmp)
#         A = [e for e in A if e % tmp != 0]
#     return p+A

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


# def make_divisors(n):
#     lower_divisors, upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]


def resolve():
    n = int(input())
    if n == 1:
        print(1)
        return

    # primes = set(get_sieve_of_eratosthenes(n))

    # result = [1]
    # tmp = 2
    # print(primes)
    # for i in range(2, n+1):
    #     # print(*result, 'next: ', i)
    #     if i in primes:
    #         # print('i is prime')
    #         result.append(2)
    #     else:
    #         # print('i is not prime')
    #         tmp += 1
    #         result.append(tmp)

    # print(*result)

    result = [1]
    tmp = 1
    for i in range(2, n+1):
        div_cnt = len(prime_factorize(i)) + 1
        # print('i:', i, ", div_cnt:", div_cnt)
        result.append(div_cnt)

    print(*result)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4"""
        output = """1 2 2 3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
