def main():
    k, g, m = list(map(int, input().split()))
    a = 0
    b = 0
    for _ in range(k):
        if a == g:
            a = 0
        elif b == 0:
            b = m
        else:
            if g-a<=b:
                b-=g-a
                a=g
            else:
                a+=b
                b=0
    print(a, b)
    


if __name__ == '__main__':
    main()
