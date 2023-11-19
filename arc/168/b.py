from collections import Counter
import math


def calc(a, k):
    return (a) % (k+1)


def check(k, A):
    grundy = []
    for a in A:
        grundy.append(calc(a, k))
    # print(k, A)
    # print(grundy)
    xor_total = 0
    for a in grundy:
        xor_total ^= a
    if xor_total == 0:
        return False
    else:
        return True


def main():
    n = int(input())
    A = list(map(int, input().split()))

    xor = 0
    for a in A:
        xor ^= a

    if xor != 0:
        print(-1)
        return

    odds = []
    for val, cnt in Counter(A).items():
        if cnt % 2 == 1:
            odds.append(val)

    if not odds:
        print(0)
    else:
        print(max(odds)-1)


if __name__ == '__main__':
    main()
