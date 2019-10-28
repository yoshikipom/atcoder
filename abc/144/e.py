import math


def check(A, F, x, N, K):
    for i in range(N):
        if A[i] * F[i] > x:
            k = math.ceil(A[i] - x / F[i])
            K -= k
    if K < 0:
        return False
    else:
        return True


def resolve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    F = list(map(int, input().split()))
    A.sort(reverse=True)
    F.sort()

    # binary search
    l = 0
    r = max(A) * max(F)
    result = None
    while l <= r:
        # print('l {}, r {}'.format(l, r))
        if l == r:
            result = l
            break
        mid = (l + r) // 2
        if check(A, F, mid, N, K):
            r = mid
        else:
            l = mid + 1

    print(result)


if __name__ == "__main__":
    resolve()
