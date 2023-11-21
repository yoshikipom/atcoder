from collections import defaultdict
import collections


def main():
    n, m = list(map(int, input().split()))
    xy = []
    for _ in range(m):
        x, y = list(map(int, input().split()))
        x-=1
        y-=1
        xy.append((x, y))
        
    RED_MAP = [False for _ in range(n)]
    RED_MAP[0] = True
    
    d = defaultdict(lambda: 1)
    
    for x, y in xy:
        # print(d, RED_MAP)
        if RED_MAP[x]:
            RED_MAP[y] = True
        d[x] -= 1
        d[y] += 1
        if d[x] == 0:
            RED_MAP[x] = False
        
            
    print(collections.Counter(RED_MAP)[True])

if __name__ == '__main__':
    main()
