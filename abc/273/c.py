from bisect import bisect


import bisect

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    # print(A)

    d = {}
    for a in A:
        if a not in d:
            d[a] = 0
        d[a] += 1

    d = sorted(d.items(), reverse=True)
    # print(d)

    for k, v in d:
        print(v)

    for i in range(len(d), n):
        print(0)

    # result = 0
    # for i in range(n):
    #     index = bisect.bisect(A, i)
    #     print(index)
    


if __name__ == '__main__':
    main()
