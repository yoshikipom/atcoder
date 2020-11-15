MOD = 10 ** 9 + 7


class Point:
    def __init__(self):
        self.left = 0
        self.up = 0
        self.upper_left = 0
        self.value = 0


h, w = list(map(int, input().split()))
MAP = []
for _ in range(h):
    row = input()
    MAP.append(row)

results = [[Point() for j in range(w+1)] for i in range(h+1)]

results[1][1].left = 0
results[1][1].up = 0
results[1][1].upper_left = 0
results[1][1].value = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        if i == 1 and j == 1:
            continue

        target = results[i][j]
        if MAP[i-1][j-2] != '#':
            target.left = (results[i][j-1].left + results[i][j-1].value) % MOD
        if MAP[i-2][j-1] != '#':
            target.up = (results[i-1][j].up + results[i-1][j].value) % MOD
        if MAP[i-2][j-2] != '#':
            target.upper_left = (results[i-1][j -
                                              1].upper_left + results[i-1][j-1].value) % MOD
        target.value = (target.left + target.up + target.upper_left) % MOD


# for row in results:
    # print(*list(map(lambda x: x.value, row)))

print(results[h][w].value)
