a, b, c = list(map(int, input().split()))

dp = [[[0 for k in range(101)] for j in range(101)] for i in range(101)]

dp[a][b][c] = 1

for i in range(a, 100):
    for j in range(b, 100):
        for k in range(c, 100):
            if i == 0 and j == 0 and k == 0:
                continue
            s = i + j + k
            dp[i+1][j][k] += dp[i][j][k] * (i / s)
            dp[i][j+1][k] += dp[i][j][k] * (j / s)
            dp[i][j][k+1] += dp[i][j][k] * (k / s)

result = 0
for i in range(0, 101):
    for j in range(0, 101):
        A = (100-a + i-b + j-c)
        if A > 0:
            result += dp[100][i][j] * A
        B = (j-a + 100-b + i-c)
        if B > 0:
            result += dp[j][100][i] * B
        C = (i-a + j-b + 100-c)
        if C > 0:
            result += dp[i][j][100] * C

print(result)
