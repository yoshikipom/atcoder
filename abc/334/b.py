from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

a, m, l, r = list(map(int, input().split()))
l -= a
r -= a

ll = (l-1)//m
rr = r//m

print(rr-ll)
