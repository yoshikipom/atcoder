def main():
    b = int(input())
    for i in range(1, 16):
        if b == i ** i:
            print(i)
            return
        
    print(-1)
    return


if __name__ == '__main__':
    main()
