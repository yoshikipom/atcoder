# -*- coding: utf-8 -*-
import sys
import os
import copy


def solve():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    s_set = []
    count = 0
    s = []

    a = []
    k = 0
    while pow(2, k) < N * K:
        ak = []

        if k == 0:
            for i in range(N):
                for j in range(1, N+1):
                    if(A[i] == A[(i+j) % N]):
                        width = j + 1
                        break
                ak.append(width)
        else:
            for i in range(N):
                step1 = a[k-1][i]
                step2 = a[k-1][(i + step1) % N]
                width = step1 + step2
                ak.append(width)

        a.append(ak)
        k += 1

    now = 0
    for e in range(k)[::-1]:
        if now + a[e][now % N] > N*K:
            continue
        now = now + a[e][now % N]

    # print(now)

    S = []
    for i in range(now, N*K):
        if A[i % N] not in S:
            S.append(A[i % N])
        else:
            for j in range(len(S)):
                if(S[j] == A[i % N]):
                    S = S[:j]
                    break

    print(' '.join(map(str, S)))


solve()

# test_path = 'test_case'
# FILES = os.listdir(test_path)
# print('test case => %s\n**********' % FILES)
# for FILE in FILES:
#     fdr = os.open(test_path + '/' + FILE, os.O_RDONLY)
#     print("\ncase : %s" % FILE)
#     os.dup2(fdr, sys.stdin.fileno())
#     solve()

# print("\n**********\nfinish")
