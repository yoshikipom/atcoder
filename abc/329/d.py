from collections import defaultdict
import heapq


def main():
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))

    q = []
    d = defaultdict(int)
    for i, a in enumerate(A):
        d[a] += 1
        heapq.heappush(q, (-d[a], a))
        cnt, num = heapq.heappop(q)
        print(num)
        heapq.heappush(q, (cnt, num))


if __name__ == '__main__':
    main()
