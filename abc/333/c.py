def main():
    n = int(input())
    
    reps = []
    for i in range(1, 15):
        reps.append(int('1'*i))
    
    # print(reps)

    def calc(a, b, c):
        return reps[a]+reps[b]+reps[c]
    
    a = 0
    b = 0
    c = 0
    cnt = 0
    while cnt < n-1:
        # print(a, b, c, calc(a,b,c))
        if a == b == c:
            c = a+1
            a = 0
            b = 0
        elif a == b and b < c:
            b+=1
            a=0
        elif a < b:
            a+=1
        cnt += 1
    
    print(calc(a,b,c))

if __name__ == '__main__':
    main()
