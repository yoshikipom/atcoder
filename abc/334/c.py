from collections import defaultdict
import itertools
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

n,k = list(map(int, input().split()))
A = list(map(int, input().split()))
if k % 2 == 0:
    result = 0
    for i in range(0,k,2):
        result += A[i+1]-A[i]
    print(result)
else:
    B = []
    for i in range(0,k-1,2):
        B.append(A[i+1]-A[i])
    C = []
    for i in range(1,k-1,2):
        C.append(A[i+1]-A[i])
    B = [0]+list(itertools.accumulate(B))
    C = [0]+list(itertools.accumulate(C[::-1]))
    result = float('inf')
    for i in range(len(B)):
        # print(i)
        result = min(result, B[i]+C[len(C)-1-i])
    print(result)
