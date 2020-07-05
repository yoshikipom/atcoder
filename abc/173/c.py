H, W, K = list(map(int, input().split()))
C = []
for _ in range(H):
    row = input()
    C.append(row)


def check(use_rows, use_cols):
    count = 0
    for i in range(H):
        if i in use_rows:
            continue
        for j in range(W):
            if j in use_cols:
                continue
            if C[i][j] == '#':
                count += 1
    return count


count = 0
for bit_row in range(2 ** H):
    use_rows = set()
    for i in range(H):
        if (bit_row >> i & 1):
            use_rows.add(i)

    for bit_col in range(2 ** W):
        use_cols = set()
        for j in range(W):
            if (bit_col >> j & 1):
                use_cols.add(j)

        # print(bit_row, bit_col, use_rows, use_cols)
        if K == check(use_rows, use_cols):
            # print(use_rows, use_cols)
            count += 1

print(count)
