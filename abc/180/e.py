INF = float('inf')

# input
N = int(input())
P = []
for _ in range(N):
    p = list(map(int, input().split()))
    P.append(p)
MAP = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        s = P[i]
        t = P[j]
        a, b, c = s
        p, q, r = t
        d = abs(p-a) + abs(q-b) + max(0, r-c)
        MAP[i][j] = d


for k in range(N):
    for i in range(N):
        for j in range(N):
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])


# for row in MAP:
#     print(*row)

# solve by DP
# dp[staus(bit)][last distnation]: cost bitは1のところが到達前
dp = [[INF for _ in range(N)] for _ in range(1 << N)]
dp[(1 << N) - 1][0] = 0

for status in range((1 << N) - 1, -1, -1):

    # 出発点と到着点を全組み合わせ試す
    for dist in range(N):
        for prev in range(N):

            # prevが到達前のときは無視
            if (status >> prev) & 1:
                continue

            prev_status = status | 1 << prev
            next_cost = dp[prev_status][prev] + MAP[prev][dist]
            dp[status][dist] = min(dp[status][dist], next_cost)

print(dp[0][0])
