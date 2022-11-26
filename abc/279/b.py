def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print('No')
        return
    
    d = len(s) - len(t)
    for l in range(d+1):
        r = l + len(t)
        # print(l, r)
        if s[l:r] == t:
            print('Yes')
            return
    
    print('No')
    return



if __name__ == '__main__':
    main()
