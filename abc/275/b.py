MOD = 998244353


def main():
    a, b, c, d, e, f = list(map(int, input().split()))
    a %= MOD
    b %= MOD
    c %= MOD
    d %= MOD
    e %= MOD
    f %= MOD

    abc_value = (((a * b) % MOD) * c) % MOD
    def_value = (((d * e) % MOD) * f) % MOD
    result = (abc_value - def_value) % MOD
    print(result)


if __name__ == '__main__':
    main()
