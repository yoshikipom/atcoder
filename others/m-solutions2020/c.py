n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

k -= 1

for i in range(k+1, n):
    if A[i-k-1] < A[i]:
        print('Yes')
    else:
        print('No')
