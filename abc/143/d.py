import bisect


def bs(L, left, right, bc):
    while left != right:
        mid = (left + right)//2
        if L[mid] > bc:
            right = mid
        else:
            left = mid+1
    if L[left] <= bc:
        return -1
    return left


def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(1, N-1):
        for j in range(i + 1, N):
            div = bisect.bisect_right(L[0:i], L[j] - L[i])
            if (div != -1):
                count += i - div

    print(count)


if __name__ == "__main__":
    solve()
