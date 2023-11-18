def main():
    n = int(input())
    s = input()
    
    last_x = -1
    last_o = -1
    
    result = 0
    for r in range(n):
        c = s[r]
        if c == 'o':
            last_o = r
            if last_x == -1:
                continue
            result += last_x+1
        elif c == 'x':
            last_x = r
            if last_o == -1:
                continue
            result += last_o+1
        else:
            raise Exception('error')
        # print(r, result, last_o, last_x)
    
    print(result)
    


if __name__ == '__main__':
    main()
