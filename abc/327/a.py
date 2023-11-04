def main():
    n = int(input())
    s = input()
    
    prev = s[0]
    for c in s[1:]:
        if prev == 'a' and c == 'b' or prev == 'b' and c == 'a':
            print('Yes')
            return
        prev = c
    
    print('No')
    return
        

if __name__ == '__main__':
    main()
