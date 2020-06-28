import copy

D = int(input())
C = list(map(int, input().split()))
S = []
for _ in range(D):
    s_row = list(map(int, input().split()))
    S.append(s_row)

V = []
for _ in range(D):
    v = int(input())
    V.append(v)

results = []

# 次の日に減る分も考慮して選ぶ
last = [0 for i in range(26)]
next_costs = [0 for i in range(26)]

result = 0
for d in range(D):
    for i in range(26):
        next_costs[i] = C[i] * (d+1-last[i])

    index = V[d] - 1
    next_costs_sum = sum(next_costs)
    result += S[d][index] - (next_costs_sum - C[index] * (d+1-last[index]))
    last[index] = d + 1
    results.append(result)

for result in results:
    print(result)
