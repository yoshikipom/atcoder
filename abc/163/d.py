N, K = list(map(int, input().split()))

left = 0
right = 0
A = []
for k in range(0, N+1):
    left += k
    right += N - k
    A.append((right - left + 1) % (10 ** 9 + 7))

# print(A)
print(sum(A[K-1:]) % (10 ** 9 + 7))
