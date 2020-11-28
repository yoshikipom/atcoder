import math
from decimal import *
import scipy

getcontext().prec = 100


def calc(a, b, c):
    D = Decimal(b*b - 4*a*c).sqrt()
    x_1 = Decimal(-b + D) / Decimal(2 * a)
    x_2 = Decimal(-b - D) / Decimal(2 * a)

    return x_1, x_2


def solve(n):
    tmp = calc(Decimal(1), Decimal(-2*n-3), Decimal(n)
               * Decimal(n) + Decimal(n))[1]

    x = tmp
    with localcontext() as ctx:
        ctx.prec = 10*20
        ctx.rounding = ROUND_CEILING
        result = x.to_integral_exact()

    print(result)


if __name__ == "__main__":
    n = int(input())
    solve(n)
