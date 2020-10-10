h, w = list(map(int, input().split()))
S = [input() for _ in range(h)]

cnt = 0
for i in range(h):
    for j in range(w-1):
        if S[i][j] == '.' and S[i][j+1] == '.':
            cnt += 1

for i in range(h-1):
    for j in range(w):
        if S[i][j] == '.' and S[i+1][j] == '.':
            cnt += 1

print(cnt)
