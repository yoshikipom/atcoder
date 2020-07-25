
A, B, C = list(map(int, input().split()))
K = int(input())

b_cnt = 0
while A >= B:
    B *= 2
    b_cnt += 1

c_cnt = 0
while B >= C:
    C *= 2
    c_cnt += 1

# print(A, B, C)
# print(b_cnt, c_cnt)

if b_cnt + c_cnt <= K:
    print('Yes')
else:
    print('No')
