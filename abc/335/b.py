from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True

def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

n = int(input())

for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            if x + y + z <= n:
                print(x, y, z)
