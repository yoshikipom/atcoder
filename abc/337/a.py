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
X = []
Y = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)
    
x_sum = sum(X)
y_sum = sum(Y)

if x_sum == y_sum:
    print('Draw')
elif x_sum > y_sum:
    print('Takahashi')
else:
    print('Aoki')
