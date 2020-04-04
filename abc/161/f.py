def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors


if __name__ == "__main__":
    N = int(input())
    part = len(make_divisors(N-1)) - 1
    cnt = 0
    for k in make_divisors(N):
        if k == 1:
            continue
        tmp_n = N
        while tmp_n % k == 0:
            tmp_n /= k
        if tmp_n % k == 1:
            cnt += 1

    print(part + cnt)
