def main():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(input())

    h_ok_cnt = [None] * n
    for i in range(n):
        cnt = 0
        for j in range(n):
            if A[i][j] == 'o':
                cnt += 1
        h_ok_cnt[i] = cnt

    w_ok_cnt = [None] * n
    for j in range(n):
        cnt = 0
        for i in range(n):
            if A[i][j] == 'o':
                cnt += 1
        w_ok_cnt[j] = cnt

    # print(h_ok_cnt)
    # print(w_ok_cnt)

    result = 0
    for i in range(n):
        for j in range(n):
            if not A[i][j] == 'o':
                continue
            result += (h_ok_cnt[i]-1) * (w_ok_cnt[j]-1)

    print(result)


if __name__ == '__main__':
    main()
