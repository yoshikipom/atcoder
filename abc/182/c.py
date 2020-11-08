def solve():
    n = int(input())

    ns = str(n)
    k = len(ns)

    result = 18
    for bit in range(1 << k):
        tmp_sum = 0
        for i in range(k):
            if bit >> i & 1:
                tmp_sum += int(ns[i])
        if tmp_sum != 0 and tmp_sum % 3 == 0:
            delete_cnt = k - bin(bit).count('1')
            result = min(result, delete_cnt)

    if result == 18:
        print(-1)
    else:
        print(result)


if __name__ == "__main__":
    solve()
