N, K, Q = map(int, input().split())

score = {}
for i in range(1, N+1):
    score[i] = 0

for i in range(Q):
    winner = int(input())
    score[winner] += 1

# print(score)

for i in range(1, N+1):
    player = i
    win = K - (Q - score[player]) > 0
    if win:
        print('Yes')
    else:
        print('No')
