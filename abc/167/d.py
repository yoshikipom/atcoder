N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

used = set()
history = []

cur = 0
used.add(0)

while True:
    history.append(cur)
    next_cur = A[cur] - 1
    if next_cur in used:
        loop_start = history.index(next_cur)
        break
    used.add(next_cur)
    cur = next_cur

B = history[loop_start:]
if K <= loop_start:
    result = history[K]
else:
    result = B[(K-loop_start) % len(B)]

print(result+1)
