def main():
    n = int(input())
    s = set()
    for i in range(n):
        day = i+1
        user = input()
        if user not in s:
            print(day)
        s.add(user)



if __name__ == '__main__':
    main()
