from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True

def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

b, g = list(map(int, input().split()))

if b>g:
    print('Bat')
else:
    print('Glove')
