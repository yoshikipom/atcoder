from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

N = int(input())

M = len(bin(N-1))-2

A = [[] for i in range(M)]
for i in range(1, N):
    for j in range(M):
        if i>>j&1:
            A[j].append(i)

A = A[::-1]        
    
# debug(A)
print(len(A))
for row in A:
    print(len(row), *row)

S = input()

result = int(S, base=2)
if result == 0:
    print(N)
else:
    print(result)
