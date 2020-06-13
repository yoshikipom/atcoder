A, V = list(map(int, input().split()))
B, W = list(map(int, input().split()))
T = int(input())

diff = abs(A - B)
diff_v = V - W


def solve():
    if diff == 0:
        return "YES"
    if diff_v <= 0:
        return "NO"

    if diff/diff_v <= T:
        return "YES"
    else:
        return "NO"


print(solve())
