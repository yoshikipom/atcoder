import collections


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def solve():
    N = int(input())
    if N == 1:
        return 0
    D = factorization(N)
    R = primes()

    result = 0
    for d in D:
        result += R[d[1]]

    return result


def primes():
    R = [0 for i in range(41)]
    for i in range(40, 0, -1):
        tmp_R = R[:]
        for j in range(i, 41):
            tmp_R[j] = max(R[j], R[j - i] + 1)
        R = tmp_R

    return R


if __name__ == "__main__":
    print(solve())
