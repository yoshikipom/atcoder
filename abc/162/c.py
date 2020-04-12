import fractions


if __name__ == "__main__":
    K = int(input())

    d = {}

    result = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            gcd_ab = fractions.gcd(i, j)
            if gcd_ab not in d:
                d[gcd_ab] = 0
            d[gcd_ab] += 1

    for gcd_ab, count in d.items():
        for k in range(1, K+1):
            result = result + fractions.gcd(gcd_ab, k) * count

    print(result)
