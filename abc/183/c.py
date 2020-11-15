import itertools

n, k = list(map(int, input().split()))
A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

result = 0
for perm in list(itertools.permutations(range(1, n))):
    cur = 0
    tmp = 0
    for next_cur in perm:
        tmp += A[cur][next_cur]
        cur = next_cur
    tmp += A[cur][0]
    # print(perm, tmp)
    if tmp == k:
        result += 1

print(result)
