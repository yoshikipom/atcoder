if __name__ == "__main__":
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    sum_all = sum(A)
    cnt = 0
    for a in A:
        if a >= sum_all/(4*m):
            cnt += 1

    if cnt >= m:
        print('Yes')
    else:
        print('No')
