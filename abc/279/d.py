def t(a, b, x):
    return b * x + a / pow(1+x, 1/2)

def main():
    a, b = list(map(int, input().split()))

    l = 0
    r = 10 ** 18
    while l+2 < r:
        c1=l+(r-l)//3
        c2=r-(r-l)//3
        # print(c1, c2)
        if t(a, b, c1)<t(a, b, c2):
            r=c2
        else:
            l=c1
        
    # print(a,b,l,r)
    print(min(t(a, b, l), t(a, b, l+1), t(a, b, r)))




if __name__ == '__main__':
    main()
    # print(t(10, 1, 0))
    # print(t(10, 1, 1))
    # print(t(10, 1, 2))
    # print(t(10, 1, 3))
    # print(t(10, 1, 4))
