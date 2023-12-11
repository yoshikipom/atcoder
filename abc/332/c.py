def main():
    n, m = list(map(int, input().split()))
    s = input()

    for i in range(n+1):
        
        a = m
        b = i
        possible=True
        # simulation
        for c in s:
            if c=='0':
                a=m
                b=i
            elif c=='1':
                if a>0:
                    a-=1
                elif b>0:
                    b-=1
                else:
                    possible=False
            elif c=='2':
                if b>0:
                    b-=1
                else:
                    possible=False
            else:
                raise Exception("error")
        
        if possible:
            print(i)
            break
                    
if __name__ == '__main__':
    main()
