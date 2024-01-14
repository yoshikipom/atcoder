from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
# DEBUG = True

def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

n = int(input())
A = list(map(int, input().split()))

R = [None] * n
L = [None] * n

R[0] = 1
for i in range(1, n):
    a = A[i]
    if a > R[i-1]:
        R[i] = R[i-1]+1
    else:
        R[i] = a
    
debug(R)
    
L[n-1] = 1
for i in range(n-1)[::-1]:
    a = A[i]
    if a > L[i+1]:
        L[i] = L[i+1]+1
    else:
        L[i] = a

debug(L)

result = 1
for i in range(1, n-1):
    num = min(R[i], L[i])
    result = max(result, num)
print(result)
