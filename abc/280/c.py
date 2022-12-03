def main():
    s = input()
    t = input()
    result = None
    for i in range(len(s)):
        if s[i] != t[i]:
            result = i + 1
            # print('get', i)
            break
    if result == None:
        result = len(t)

    print(result)


if __name__ == '__main__':
    main()
