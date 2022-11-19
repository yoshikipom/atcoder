def main():
    n, x = list(map(int, input().split()))
    P = list(map(int, input().split()))
    for i in range(n):
        if P[i] == x:
            print(i+1)


if __name__ == '__main__':
    main()
