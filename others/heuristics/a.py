import copy

D = int(input())
C = list(map(int, input().split()))
S = []
for _ in range(D):
    s_row = list(map(int, input().split()))
    S.append(s_row)

results = []

# Cを無視して最大値をとる
# for d in range(D):
#     s_row = S[d]
#     max_value = max(s_row)
#     max_index = s_row.index(max_value)
#     results.append(max_index+1)

# 26種類順番にやる
# for d in range(D):
#     results.append((d % 26) + 1)
#     results.append(max_index+1)

# 次の日に減る分も考慮して選ぶ
last = [0 for i in range(26)]
next_costs = [0 for i in range(26)]

for d in range(D):

    for i in range(26):
        next_costs[i] = C[i] * (d+1-last[i])

    result = -100000
    next_costs_sum = sum(next_costs)
    result_idx = -1
    for i in range(26):
        tmp_result = S[d][i] - (next_costs_sum - C[i] * (d+1-last[i]))
        if tmp_result > result:
            result = tmp_result
            result_idx = i
    last[result_idx] = d + 1
    results.append(result_idx + 1)

for result in results:
    print(result)
