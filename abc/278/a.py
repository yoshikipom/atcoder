from collections import deque


def main():
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    q = deque(A)
    for i in range(k):
        q.popleft()
        q.append(0)

    print(*q)


if __name__ == '__main__':
    main()
