from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True

def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

s = input()
print(s[:-1]+'4')
