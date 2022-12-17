def main():
    s: str = input()

    if len(s) != 8:
        print('No')
        return

    if not s[0].isalpha() or not s[0].isupper():
        print('No')
        return

    if s[1] == '0':
        print('No')
        return 
    
    for i in range(1, 7):
        if not s[i].isnumeric():
            print('No')
            return

    if not s[7].isalpha() or not s[7].isupper():
        print('No')
        return

    print('Yes')


if __name__ == '__main__':
    main()
