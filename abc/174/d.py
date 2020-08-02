N = int(input())
S = input()

l = 0
r = len(S) - 1

W = 'W'
R = 'R'

cnt = 0
while l < r:
    if S[l] == R:
        l += 1
        continue
    else:
        while l < r:
            if S[r] == W:
                r -= 1
                continue
            else:
                cnt += 1
                l += 1
                r -= 1
                break

print(cnt)
