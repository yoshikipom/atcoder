def solve():
    n, k = map(int, input().split())

    tmp = n % k
    return min([tmp, n, k, k - tmp])


if __name__ == "__main__":
    result = solve()
    print(result)
