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
    # print(L)
    count = 0
    for i in range(1, N-1):
        for j in range(i + 1, N):
            left = 0
            right = i-1
            div = bs(L, left, right, L[j] - L[i])
            if (div != -1):
                count += i - div
                # print('counted')
                # print(i-div)

    print(count)


if __name__ == "__main__":
    solve()
    # L = [1, 2, 3, 4, 5, 6]
    # print(bs(L, 0, 3, 1))
