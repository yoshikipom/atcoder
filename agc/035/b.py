# -*- coding: utf-8 -*-
import sys
import os


def solve():
    N, M = list(map(int, input().split()))
    edge = {}
    for i in range(M):
        a, b = list(map(int, input().split()))
        if a not in edge.keys():
            edge[a] = set()
        if b not in edge.keys():
            edge[b] = set()
        edge[a].add(b)
        edge[b].add(a)

    print(edge)

    if M % 2 == 0:
        print(-1)
        return

    C = []
    D = []
    while len(edge) != 0:
        for point_from, point_to_list in edge.items():
            if len(point_to_list) >= 2:
                for point_to in point_to_list:
                    if len(edge[point_to]) == 1:

                edge[point_from].remove(v)
                edge[v].remove(point_from)
                C.append(point_from)
                D.append(point_from)
                break

            # tmp = 0
            # for a in A:
            # tmp = tmp ^ a

            # if tmp == 0:
            # print('Yes')
            # else:
            # print('No')


solve()
