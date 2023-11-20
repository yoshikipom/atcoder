global n, p, k, A
n, p, k = list(map(int, input().split()))
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
    
    
def warshall(Dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                Dist[i][j] = min(Dist[i][j], Dist[i][k]+Dist[k][j])
                
def check(x, f):
    Dist = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][j] == -1:
                Dist[i][j] = x
            else:
                Dist[i][j] = A[i][j]
    warshall(Dist)
    cnt = 0
    for i in range(n):
      for j in range(i+1, n):
        if Dist[i][j] <= p:
          cnt += 1
    
    if cnt >= k+f:
        return True
    else:
        return False

                
def bin_search(l, r, f):
    while r - l > 1:
        mid = (l+r)//2
        if check(mid, f):
            l = mid
        else:
            r = mid
    return l


def main():
    l = bin_search(0, 10**10+1, 1)
    r = bin_search(0, 10**10+1, 0)
    
    if l != 10**10 and r == 10**10:
        result = 'Infinity'
    elif r == l == 10**10:
        result = 0
    else:
        result = r - l
    print(result)


if __name__ == '__main__':
    main()
