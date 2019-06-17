

import queue


def check():
    for i in range(H):
        if '.' in A[i]:
            return False
    return True


if __name__ == "__main__":
    s = set()
    H, W = map(int, input().split())
    A = []
    a_row_flame = ['!'] * (W+2)
    A.append(a_row_flame)
    for i in range(H):
        row = input()
        a_row = []
        a_row.append('!')
        for j in range(W):
            if row[j] == '.':
                a_row.append('.')
            else:
                a_row.append('#')
                s.add((i+1, j+1))
        a_row.append('!')
        A.append(a_row)
    A.append(a_row_flame)

    count = 0
    while True:
        # print(A)
        tmp_s = set()
        for pair in s:
            i = pair[0]
            j = pair[1]
            if A[i-1][j] == '.':
                tmp_s.add((i-1, j))
            if A[i+1][j] == '.':
                tmp_s.add((i+1, j))
            if A[i][j-1] == '.':
                tmp_s.add((i, j-1))
            if A[i][j+1] == '.':
                tmp_s.add((i, j+1))

        for pair in tmp_s:
            A[pair[0]][pair[1]] = '#'

        if len(tmp_s) is 0:
            break
        else:
            count += 1
            s = tmp_s

    print(count)
