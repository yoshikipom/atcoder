from itertools import combinations

n, m = list(map(int, input().split()))

S_list = []

for i in range(m):
    S = list(map(int, input().split()))[1:]
    S_list.append(set(S))



result = True
for a,b in list(combinations(range(1, n+1),2)):

    tmp_result = False
    for S in S_list:
        if a in S and b in S:
            tmp_result = True
            break
    if not tmp_result:
        result = False
        break

if result:
    print('Yes')
else:
    print('No')
