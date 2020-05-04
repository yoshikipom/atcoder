from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))

li = []
for i in range(N):
    li.append(A[i] + i)

li.sort()

cnt = 0
for j in range(N):
    target = j - A[j]
    cnt += bisect_right(li, target) - bisect_left(li, target)

print(cnt)
