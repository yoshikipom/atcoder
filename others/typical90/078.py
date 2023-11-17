import bisect
from collections import defaultdict


def main():
    n, m = list(map(int, input().split()))
    d = defaultdict(list)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        d[a].append(b)
        d[b].append(a)
    
    result = 0
    for k, v in d.items():
        cnt = 0
        for a in v:
            if a < k:
                cnt += 1
        if cnt == 1:
            result += 1
    
    print(result)
        


if __name__ == '__main__':
    main()
