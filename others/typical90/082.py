import math

MOD = 10**9+7


def total(L, R):
    if L > R:
        return 0
    else:
        sum = ((R - L + 1) * (L + R)) // 2
        return sum


def main():
    L, R = list(map(int, input().split()))
    result = 0
    for base in range(19):
        # [10^base, 10^(base+1))
        l = 10**base
        r = 10**(base+1)

        result += total(max(L, l), min(R, r-1)) * (base+1)
        result %= MOD

        # print(base, result, max(L,l), min(R,r-1))
    print(result)


if __name__ == '__main__':
    main()
