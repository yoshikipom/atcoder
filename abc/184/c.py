r1, c1 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))


def solve():
    if r1 == r2 and c1 == c2:
        return 0

    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    if r1 + c1 == r2 + c2:
        return 1
    if r1 - c1 == r2 - c2:
        return 1

    if (r1 + c1) % 2 == (r2 + c2) % 2:
        return 2

    x = r2 - r1
    y = c2 - c1

    if y <= x + 3 and y >= x - 3:
        return 2
    if y <= -x + 3 and y >= -x - 3:
        return 2

    return 3


if __name__ == "__main__":
    print(solve())
