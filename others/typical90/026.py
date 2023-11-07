from collections import defaultdict, deque


def main():
    n = int(input())
    # A = [None] * n
    # B = [None] * n
    # for i in range(n):
    #     A[i], B[i] = list(map(int, input().split()))
    d = defaultdict(list)
    
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        d[a].append(b)
        d[b].append(a)
        
    q = deque()
    q.appendleft((1,0))
    levels = defaultdict(list)
    seen = set()
    while q:
        cur, level = q.pop()
        if cur in seen:
            continue
        seen.add(cur)
        levels[level%2].append(cur)
        for next_cur in d[cur]:
            if next_cur in seen:
                continue
            q.appendleft((next_cur, level+1))
            
    # print(levels)
    if len(levels[0]) >= n//2:
        print(*levels[0][:n//2])
    else:
        print(*levels[1][:n//2])


if __name__ == '__main__':
    main()
