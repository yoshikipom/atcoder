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
s = bin(n)

result = 0
for c in s[::-1]:
    if c != '0':
        break
    else:
        result+=1
        
print(result)
        
        
