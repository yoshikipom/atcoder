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
s = 'L' + 'o' * n + 'n' + 'g'
print(s)
