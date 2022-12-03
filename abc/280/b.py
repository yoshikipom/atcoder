def main():
    n = int(input())
    S = list(map(int, input().split()))
    A = []
    prev = 0
    for s in S:
        A.append(s-prev)
        prev = s
        # print(s, prev)
        
    print(*A)


if __name__ == '__main__':
    main()
