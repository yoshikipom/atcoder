if __name__ == "__main__":
    n = int(input())
    result = False
    while True:
        if n % 10 == 7:
            result = True
        n //= 10
        if n == 0:
            break

    if result:
        print('Yes')
    else:
        print('No')
