def main():
    n, k = list(map(int, input().split()))
    x = n
    d = {}
    d[x] = 0
    turn = 0
    
    while turn < k:
        y = 0
        for c in str(x):
            y += int(c)
        x += y
        x %= 10**5

        turn += 1
        
        # ループしてるなら一気にすすめる
        if x in d:
            # print('loop!', turn, x)
            loop_length = turn - d[x]
            loop_count = (k - turn) // loop_length
            turn += loop_length * loop_count
        else:
            d[x] = turn

        # print(x)

    print(x)


if __name__ == '__main__':
    main()
