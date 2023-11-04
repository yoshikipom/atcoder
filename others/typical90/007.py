import bisect


def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    B = []
    for _ in range(q):
        B.append(int(input()))
    
    A.sort()
    
    for b in B:
        index = bisect.bisect_left(A, b)
        if index == 0:
            result = abs(A[index]-b)
        elif index == n:
            result = abs(A[index-1]-b)
        else:
            result = min(abs(A[index]-b), abs(A[index-1]-b))
        print(result)


if __name__ == '__main__':
    main()
