

# def binary_search():


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    # for i in range(n):
    # A[i] *= 10**10

    def f(x):
        tmp = 0
        for a in A:
            tmp += a - min(a, 2*x)
        return n * x + tmp

    l, r = 0, 10**18
    while l+pow(10, -7) < r:
        c1 = l+(r-l)/3
        c2 = r-(r-l)/3
        if f(c1) < f(c2):
            r = c2
        else:
            l = c1
        # print(l, r)
    print(f(l)/n)


if __name__ == '__main__':
    resolve()
