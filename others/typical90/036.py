# def main_TLE():
#     n, q = list(map(int, input().split()))
#     XY = [None]
#     for _ in range(n):
#         XY.append(list(map(int, input().split())))
        
#     M = [[0 for _ in range(n+1)] for _ in range(n+1)]
#     for i in range(1, n+1):
#         pi = XY[i]
#         for j in range(i+1, n+1):
#             pj = XY[j]
#             M[i][j] = abs(pi[0]-pj[0]) + abs(pi[1]-pj[1])
#             M[j][i] = abs(pi[0]-pj[0]) + abs(pi[1]-pj[1])
            
#     for _ in range(q):
#         target = int(input())
#         print(max(M[target]))
        
INF = float('inf')

def main():
    n, q = list(map(int, input().split()))
    XY = []
    min_x = INF
    min_y = INF
    max_x = -INF
    max_y = -INF
    for _ in range(n):
        x,y = list(map(int, input().split()))
        # 45度回転
        x, y = x-y, x+y
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        XY.append((x,y))
    
    for _ in range(q):
        target = int(input()) - 1
        x, y = XY[target]
        result = max(
            [
                abs(x-min_x),
                abs(y-min_y),
                abs(x-max_x),
                abs(y-max_y),
            ]
        )
        print(result)


if __name__ == '__main__':
    main()
