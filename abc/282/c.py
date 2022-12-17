def main():
    n = int(input())
    S = input()
    
    s = []
    for c in S:
        s.append(c)
    
    inside = False
    for i, c in enumerate(s):
        if inside:
            if c == '"':
                inside = False
        else:
            if c == '"':
                inside = True
            if c == ',':
                s[i] = '.'
                    
    print(''.join(s))



if __name__ == '__main__':
    main()
