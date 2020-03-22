def sum_solve(d):
    result = 0
    for k, v in d.items():
        result += v * (v-1) / 2
    return int(result)


def solve(sum_d, d, except_num):
    num = d[except_num]
    result = sum_d - num * (num-1)/2 + (num-1) * (num-2) / 2
    return int(result)


N = int(input())
A = list(map(int, input().split()))

d = {}

for a in A:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1

sum_d = sum_solve(d)
# print(sum_d)

for i, a in enumerate(A):
    print(solve(sum_d, d, a))
