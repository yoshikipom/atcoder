# WA for some case
from collections import deque

import sys
import math

INF = float('inf')


def find_available_basic_moves(N, M):
    li = []

    b = math.sqrt(M)
    if b.is_integer():
        li.append((int(b), 0))

    for i in range(math.ceil(b)):
        if M <= pow(i, 2):
            continue
        j = math.sqrt(M - pow(i, 2))
        if j.is_integer() and int(i) != b and int(j) != b:
            li.append((int(i), int(j)))
            break
    return li


def convert_to_moves(basic_moves):
    s = set()
    for basic_move in basic_moves:
        s.add((basic_move[0], basic_move[1]))
        s.add((-basic_move[0], basic_move[1]))
        s.add((basic_move[0], -basic_move[1]))
        s.add((-basic_move[0], -basic_move[1]))
        s.add((basic_move[1], basic_move[0]))
        s.add((-basic_move[1], basic_move[0]))
        s.add((basic_move[1], -basic_move[0]))
        s.add((-basic_move[1], -basic_move[0]))
    return s


N, M = list(map(int, input().split()))
D = [[-1 for i in range(N)] for j in range(N)]
D[0][0] = 0

# for row in D:
#     print(*row)

basic_moves = find_available_basic_moves(N, M)

if not basic_moves:
    # for i in range(N):
    #     for j in range(N):
    #         if D[i][j] == INF:
    #             D[i][j] = -1
    for row in D:
        print(*row)
    sys.exit(0)

moves = convert_to_moves(basic_moves)
# print(f'move {moves}')

queue = deque()
queue.append((0, 0, 0))
while queue:
    # print(queue)
    cost, i, j = queue.popleft()
    next_cost = cost + 1

    for basic_moves in moves:
        dx = basic_moves[0]
        dy = basic_moves[1]
        next_i = i + dx
        next_j = j + dy
        # print(next_i, next_j)
        if 0 <= next_i and next_i < N and 0 <= next_j and next_j < N:
            if D[next_i][next_j] == -1:
                D[next_i][next_j] = next_cost
                queue.append((next_cost, next_i, next_j))

for row in D:
    print(*row)
