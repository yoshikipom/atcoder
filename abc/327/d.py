from collections import defaultdict, deque


def main():
    n, m = list(map(int, input().split()))
    d = defaultdict(list)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(m):
        # TODO: 重複排除 if necessary
        d[A[i]].append(B[i])
        d[B[i]].append(A[i])
        
    # print(d)
    
    seen = set()
    M = [None] * (n+1)
    for start in A:
        # print(start, seen)
        if start in seen:
            continue
        q = deque()
        q.appendleft((start,True))
        
        while q:
            cur, tf = q.pop()
            if cur in seen:
                continue
            seen.add(cur)
            M[cur] = tf
            
            for next_cur in d[cur]:
                if M[next_cur] == tf:
                    return 'No'
                q.appendleft((next_cur, not tf))
    
    return 'Yes'
    


if __name__ == '__main__':
    print(main())
