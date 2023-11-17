MOD = 10**9+7


def main():
    n, k = list(map(int, input().split()))
    if n == 1:
        print(k)
        return
    elif n == 2:
        print(k * (k-1))
        return
    print((k*(k-1)*pow(k-2, n-2, MOD)) % MOD)


if __name__ == '__main__':
    main()
