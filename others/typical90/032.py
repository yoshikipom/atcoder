import collections
import itertools

INF = float('inf')

def main():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    rumor = collections.defaultdict(list)
    m = int(input())
    for _ in range(m):
        x, y = list(map(int, input().split()))
        x-=1
        y-=1
        rumor[x].append(y)
        rumor[y].append(x)
        
    result = INF
    for l in itertools.permutations([i for i in range(n)], n):
        # print(l)
        prev = None
        t = 0
        for j, runner in enumerate(l):
            if runner in rumor[prev]:
                break
            prev = runner
            t+=A[runner][j]
        else:
            result = min(result, t)
            # print('ok')
    
    if result == INF:
        result = -1
    print(result)

if __name__ == '__main__':
    main()
