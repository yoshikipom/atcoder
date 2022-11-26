def main():
    h, w = list(map(int, input().split()))
    S = []
    for i in range(h):
        S.append(input())
    T = []
    for i in range(h):
        T.append(input())

    ds = {}
    dt = {}
    for i in range(w):
        s_key = []
        t_key = []
        for j in range(h):
            s_key.append(S[j][i])
            t_key.append(T[j][i])
        s_key = tuple(s_key)
        if s_key not in ds:
            ds[s_key] = 0
        ds[s_key] += 1

        t_key = tuple(t_key)
        if t_key not in dt:
            dt[t_key] = 0
        dt[t_key] += 1

    # print('ds', ds)    
    # print('dt', dt)

    result = True
    for key in ds.keys():
        if key not in dt:
            result = False
            break
        if ds[key] != dt[key]:
            result = False
            break
    if result:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
