def main():
    n = int(input())
    H = list(map(int, input().split()))
    m = max(H)
    result = None
    for i in range(n):
        if H[i] == m:
            result = i +1

    print(result)


if __name__ == '__main__':
    main()
