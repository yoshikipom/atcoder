import collections

INF = float('inf')

N, M = list(map(int, input().split()))
d = {i: [] for i in range(N)}

for _ in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    d[a].append(b)
    d[b].append(a)

queue = collections.deque()
queue.append((0, 0))
results = {i: (INF, -1) for i in range(N)}
results[0] = (0, 0)
used = set()

while queue:
    cost, cur = queue.pop()
    if cur in used:
        continue
    used.add(cur)
    next_list = d[cur]

    for next_cur in next_list:
        next_cost = cost+1
        if next_cost < results[next_cur][0]:
            results[next_cur] = (next_cost, cur)
            queue.appendleft((next_cost, next_cur))

is_no = False
for k, result in results.items():
    if k == 0:
        continue
    if result[1] == -1:
        is_no = True

if is_no:
    print('No')
else:
    print('Yes')
    for k, result in results.items():
        if k == 0:
            continue
        print(result[1] + 1)
