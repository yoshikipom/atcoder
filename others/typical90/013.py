from collections import defaultdict
import heapq


def calc_times(start, d):
    q = []
    heapq.heappush(q, (0, start))
    seen = set()
    times = {}
    times[start] = 0
    
    while q:
        # print(q)
        t, cur = heapq.heappop(q)
        if cur in seen:
            continue
        seen.add(cur)
        times[cur] = t
        for next_cur, cost in d[cur]:
            heapq.heappush(q, (t+cost, next_cur))
    return times

def main():
    d = defaultdict(list)
    n, m = list(map(int, input().split()))
    for _ in range(m):
        a,b,c = list(map(int, input().split()))
        d[a].append((b,c))
        d[b].append((a,c))

    times_from_1 = calc_times(1, d)
    times_from_n = calc_times(n, d)
    
    # print(times_from_1)
    # print(times_from_n)

    for i in range(1, n+1):
        print(times_from_1[i] + times_from_n[i])


if __name__ == '__main__':
    main()
