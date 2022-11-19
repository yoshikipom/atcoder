def main():
    h, m = list(map(int, input().split()))
    minute = h * 60 + m

    while True:
        h = str(minute // 60).zfill(2)
        m = str(minute % 60).zfill(2)
        hh = int(h[0] + m[0])
        mm = int(h[1] + m[1])
        # print(h, m, " -> ", hh, mm)
        if 0 <= hh < 24 and 0 <= mm < 60:
            print(h, m)
            break

        minute += 1
        minute %= 24 * 60


if __name__ == '__main__':
    main()
