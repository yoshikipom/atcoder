import math


def solve(n, s, k):
    a = k
    b = n-s
    m = n
    # print(a, b, m)

    tmp = math.gcd(a, b)
    d = math.gcd(tmp, m)
    a //= d
    b //= d
    m //= d
    # print(a, b, m)

    tmp = math.gcd(a, m)
    if tmp != 1:
        print(-1)
        return

    result = (pow(a, -1, m) * b) % m
    print(result)
    return


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, s, k = list(map(int, input().split()))
        solve(n, s, k)
