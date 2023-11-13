def main():
    n = int(input())
    result = 1
    for _ in range(n):
        A = list(map(int, input().split()))
        result *= sum(A)
        result %= 10**9+7
    print(result)


if __name__ == '__main__':
    main()
