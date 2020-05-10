A, B, C, K = list(map(int, input().split()))


def solve():
    global A, B, C, K
    result = 0
    if A >= K:
        return K
    K -= A
    result += A

    if B >= K:
        return result
    K -= B

    return result - K


print(solve())
