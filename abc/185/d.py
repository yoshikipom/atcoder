import math


def solve(n, m, k, B):
    can = True
    cnt = 0
    for b in B:
        if b < k:
            can = False
            break
        cnt += math.ceil(b/k)

    if not can:
        return -1
    else:
        return cnt


def binary_search(n, m, B):
    left = 1
    right = n
    result = float('inf')
    while left <= right:
        mid = (left + right) // 2
        tmp_result = solve(n, m, mid, B)
        # print('solve mid: {}, result: {}'.format(mid, tmp_result))
        if tmp_result == -1:
            right = mid - 1
        else:
            left = mid + 1
            result = min(result, tmp_result)
    return result


n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
A.append(n+1)
A.sort()
B = []
for i in range(0, m+1):
    if i == 0:
        b = A[i] - 0 - 1
        if b > 0:
            B.append(b)
    else:
        b = A[i] - A[i-1] - 1
        if b > 0:
            B.append(b)
# print(B)
print(binary_search(n, m, B))
