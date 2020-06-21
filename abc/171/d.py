N = int(input())
A = list(map(int, input().split()))
Q = int(input())

d = {}
for a in A:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
tmp_sum = sum(A)


for _ in range(Q):
    b, c = list(map(int, input().split()))
    if b in d:
        b_cnt = d[b]
    else:
        b_cnt = 0

    d[b] = 0
    if c in d:
        d[c] += b_cnt
    else:
        d[c] = b_cnt

    sum_diff = (c - b) * b_cnt
    tmp_sum += sum_diff
    print(tmp_sum)
