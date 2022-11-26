def main():
    s = input()
    result = 0
    for c in s:
        if c == 'v':
            result += 1
        elif c == 'w':
            result += 2

    print(result)

    


if __name__ == '__main__':
    main()
