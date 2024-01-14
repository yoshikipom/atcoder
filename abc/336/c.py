from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True

def debug(*args):
    if DEBUG:
        print('[Debug]', *args)
        

def to_quinary(num):
    if num == 0:
        return "0"
    digits = []
    while num:
        digits.append(str(num % 5))
        num //= 5
    return ''.join(digits[::-1])


n = int(input())
a = to_quinary(n-1)

for c in a:
    print(int(c)*2, end='')
print()
