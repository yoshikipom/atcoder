from collections import defaultdict, deque


def main():
    n = int(input())
    d = defaultdict(list)
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        d[a].append(b)
        d[b].append(a)
    
    if len(d[1]) == 1:
        print(1)
        return
    
    rem = 0
    for child in d[1]:
        seen = set()
        seen.add(1)
        q = deque()
        seen.add(child)
        q.appendleft(child)
        cnt = 0
        while q:
            cur = q.pop()
            cnt+=1
            # print('debug...', cur)
            for next_cur in d[cur]:
                if next_cur in seen:
                    continue
                seen.add(next_cur)
                q.appendleft(next_cur)
        rem = max(rem, cnt)
        # print('debug', cnt, child)
    
    print(n-rem)
        


if __name__ == '__main__':
    main()
