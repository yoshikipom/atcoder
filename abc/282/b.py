def main():
    n, m = list(map(int, input().split()))
    SS = []
    for i in range(n):
        SS.append(input())

    count = 0
    for a in range(n):
        for b in range(a+1, n):
            can_solve = True
            sa = SS[a]
            sb = SS[b]
            for j in range(m):
                if sa[j] == 'x' and sb[j] == 'x':
                    can_solve = False
                    break
            if can_solve:
                count += 1

    print(count)


if __name__ == '__main__':
    main()
