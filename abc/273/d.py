from bisect import bisect, bisect_left, bisect_right


def main():
    h, w, rs, cs = list(map(int, input().split()))
    n = int(input())
    R = [None] * n
    C = [None] * n

    wx = {}
    wy = {}

    for i in range(n):
        R[i], C[i] = list(map(int, input().split()))
        if R[i] not in wx:
            wx[R[i]] = []
        wx[R[i]].append(C[i])

        if C[i] not in wy:
            wy[C[i]] = []
        wy[C[i]].append(R[i])

    q = int(input())
    D = [None] * q
    L = [None] * q
    for i in range(q):
        D[i], L[i] = input().split()
        L[i] = int(L[i])

    for k, v in wx.items():
        v.sort()
    for k, v in wy.items():
        v.sort()

    # print(wx)
    # print(wy)

    # print(wx)
    # print(wy)

    r = rs
    c = cs
    for i in range(q):
        d = D[i]
        l = L[i]
        if d == 'L':
            if r not in wx:
                c = max(1, c - l)
                print(r, c)
                continue

            index_now = bisect_left(wx[r], c)
            index_next = bisect_left(wx[r], c - l)
            if index_now is index_next:
                c = max(1, c - l)
            else:
                c = wx[r][index_now-1] + 1
        elif d == 'R':
            if r not in wx:
                c = min(c+l, w)
                print(r, c)
                continue
            index_now = bisect_right(wx[r], c)
            index_next = bisect_right(wx[r], c + l)
            if index_now is index_next:
                c = min(c+l, w)
            else:
                c = wx[r][index_now] - 1
        elif d == 'U':
            if c not in wy:
                r = max(1, r - l)
                print(r, c)
                continue
            index_now = bisect_left(wy[c], r)
            index_next = bisect_left(wy[c], r - l)

            if index_now is index_next:
                r = max(1, r - l)
            else:
                r = wy[c][index_now-1] + 1
        if d == 'D':
            if c not in wy:
                r = min(r + l, h)
                print(r, c)
                continue
            index_now = bisect_right(wy[c], r)
            index_next = bisect_right(wy[c], r + l)
            if index_now is index_next:
                r = min(r + l, h)
            else:
                r = wy[c][index_now] - 1
        # print(d, l, ": ", r, c)
        print(r, c)
    


if __name__ == '__main__':
    main()
