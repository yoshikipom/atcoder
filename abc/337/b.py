import re
from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

DEBUG = False
DEBUG = True


def debug(*args):
    if DEBUG:
        print('[Debug]', *args)

S = input()


def match_abc_pattern(s):
    pattern = r'^A*B*C*$'
    if re.match(pattern, s):
        return True
    else:
        return False

if match_abc_pattern(S):
    print('Yes')
else:
    print('No')
