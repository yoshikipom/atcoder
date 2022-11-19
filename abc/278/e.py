from copy import deepcopy


def main():
    H, W, N, h, w = list(map(int, input().split()))
    M = []
    for i in range(H):
        M.append(list(map(int, input().split())))

    dd = {}
    for i in range(H):
        for j in range(W):
            value = M[i][j]
            if value not in dd:
                dd[value] = 0
            dd[value] += 1
    # print(dd)


    results = [[None for j in range(W-w+1)] for i in range(H-h+1)]

    for i in range(H-h+1):
        d = dd.copy()
        for ii in range(i, i + h):
            for jj in range(w):
                value = M[ii][jj]
                if value not in d:
                    continue
                if d[value] == 1:
                    d.pop(value)
                else:
                    d[value] -= 1
        results[i][0] = len(d)
        # print(i, d)
        for j in range(1, W-w+1):
            jj = j - 1
            for ii in range(i, i + h):
                value = M[ii][jj]
                if value not in d:
                    d[value] = 0
                d[value] += 1
            jj = j + w - 1
            for ii in range(i, i + h):
                value = M[ii][jj]
                if d[value] == 1:
                    d.pop(value)
                else:
                    d[value] -= 1
            results[i][j] = len(d)
            # print(d)
    
    for row in results:
        print(*row)


if __name__ == '__main__':
    main()
