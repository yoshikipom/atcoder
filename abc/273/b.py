import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


def f(n, i):
    tmp = n / (10 ** i)
    # print(tmp)
    tmp = Decimal(str(tmp)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    # print(tmp)
    return int(tmp * 10 ** i)


def main():
    x, k = list(map(int, input().split()))
    result = x
    for i in range(1, k+1):
        result = f(result, i)
        # print(i, result)
    print(result)


if __name__ == '__main__':
    main()
