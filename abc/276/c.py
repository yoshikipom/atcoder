from bisect import bisect_left
import itertools
import math


def main():
    n = int(input())
    P = list(map(int, input().split()))
    A = P.copy()
    B = P.copy()
    A.sort()
    B.sort()

    # print(P)
    # print(A)

    p_point = 0
    for i in range(n):
        index = bisect_left(A, P[i])
        p_point += index * math.factorial(n-i-1)
        A.pop(index)

    target_point = p_point
    result = []

    # print(target_point)
    for i in range(n):
        index = math.ceil(target_point / math.factorial(n-i-1))
        target_point = target_point - (math.factorial(n-i-1) * (index-1))
        result.append(B.pop(index-1))
        # print(result, 'remain', target_point)

    print(" ".join(map(str, result)))

    # print(list(itertools.permutations(list((range(1, 11)))))[p_point])


if __name__ == '__main__':
    main()
