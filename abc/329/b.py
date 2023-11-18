def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    m = A[0]
    for a in A:
        if a != m:
            print(a)
            return
    


if __name__ == '__main__':
    main()
