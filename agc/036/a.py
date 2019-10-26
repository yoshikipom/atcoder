# -*- coding: utf-8 -*-
import sys
import os
import math


def solve():
    S = int(input())

    X2 = 1
    X3 = 0
    Y3 = 0

    X1 = math.ceil(pow(S, 0.5))
    Y2 = X1
    Y1 = pow(X1, 2) - S

    print('%d %d %d %d %d %d' % (X1, Y1, X2, Y2, X3, Y3))


solve()
