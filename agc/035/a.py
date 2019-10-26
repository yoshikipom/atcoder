# -*- coding: utf-8 -*-
import sys
import os


def solve():
    N = input()
    A = list(map(int, input().split()))

    tmp = 0
    for a in A:
        tmp = tmp ^ a

    if tmp == 0:
        print('Yes')
    else:
        print('No')


solve()
