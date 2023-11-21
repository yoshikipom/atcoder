def main():
    n, k = list(map(int, input().split()))
    D = set(list(map(int, input().split())))

    for i in range(n, 10*n+1):
        possible = True
        for c in str(i):
            if int(c) in D:
                possible = False
                break
        if possible:
            print(i)
            return
                



if __name__ == '__main__':
    main()
