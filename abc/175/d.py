INF = float('inf')

n, k = list(map(int, input().split()))
P = list(map(int, input().split()))
P = list(map(lambda x: x-1, P))
C = list(map(int, input().split()))


def simulate(start, k):
    result = -INF
    cur = start
    score = 0

    turn = 0
    cycle_check = False
    while turn < k:
        turn += 1
        cur = P[cur]
        score += C[cur]
        result = max(result, score)
        # サイクル時の処理短縮
        if cur == start and cycle_check == False:
            cycle_check = True
            # １周して減ってるなら回す必要なし
            if score <= 0:
                break
            # 1周して増えるなら最後の1周 + αだけ試す
            cycle_cnt = (k // turn) - 1
            if cycle_cnt < 1:
                cycle_cnt = 0
            # break
            turn = cycle_cnt * turn
            score = cycle_cnt * score

    return result


result = -INF
for i in range(n):
    # if i != 2:
    #     continue
    result = max(result, simulate(i, k))

print(result)
