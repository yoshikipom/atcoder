from collections import OrderedDict


if __name__ == "__main__":
    N, X, Y = map(int, input().split())
    k_dict = OrderedDict()

    for i in range(1, N):
        k_dict[i] = 0

    for i in range(1, N):
        for j in range(i+1, N+1):
            if i <= X and j <= X:
                d = j - i
                k_dict[d] += 1
                # print('{} {} {} debug 1'.format(i, j, d))
                continue

            if i <= X and X < j and j < Y:
                d = min(j-i, X-i + 1 + Y-j)
                k_dict[d] += 1
                # print('{} {} {} debug 2'.format(i, j, d))
                continue

            if i <= X and Y <= j:
                d = X-i + 1 + j-Y
                k_dict[d] += 1
                # print('{} {} {} debug 3'.format(i, j, d))
                continue

            if X < i and i < Y and X < j and j < Y:
                d = min(j-i, i-X + 1 + Y-j)
                k_dict[d] += 1
                # print('{} {} {} debug 4'.format(i, j, d))
                continue

            if X < i and i < Y and Y <= j:
                d = min(j-i, i-X + 1 + j - Y)
                k_dict[d] += 1
                # print('{} {} {} debug 5'.format(i, j, d))
                continue

            if Y <= i and Y <= j:
                d = j-i
                k_dict[d] += 1
                # print('{} {} {} debug 6'.format(i, j, d))
                continue

    for k, v in k_dict.items():
        # print('{} {}'.format(k, v))
        print(v)
