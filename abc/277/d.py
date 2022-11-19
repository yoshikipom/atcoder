def main():
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    d = {}
    sum_dict = {}
    A.sort()
    for a in A:
        key = a % m
        if key not in d:
            d[key] = []
            sum_dict[key] = 0
        d[key].append(a)
        sum_dict[key] += a

    # for key, value in d.items():
    #     print(key, value, sum_dict[key])

    max_sum = 0
    done = set()
    for i in sorted(sum_dict.keys()):
        tmp = 0
        if i in done:
            continue
        for j in range(m):
            key = (i+j) % m
            done.add(key)
            if key not in sum_dict:
                break
            tmp += sum_dict[key]
        # print(i, tmp)
        max_sum = max(tmp, max_sum)

    print(sum(A) - max_sum)


if __name__ == '__main__':
    main()
