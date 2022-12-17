# def main():
#     n, m = list(map(int, input().split()))
#     U = [None] * m
#     V = [None] * m
#     for i in range(m):
#         U[i], V[i] = list(map(int, input().split()))
#         U[i] -= 1
#         V[i] -= 1
#     d = {}
#     for i in range(n):
#         d[i] = []
#     for i in range(m):
#         u = U[i]
#         v = V[i]
#         d[u].append(v)
#         d[v].append(u)

#     # print(d)
#     mark = [None] * n

#     def dfs(v, c, count):
#         # print(mark, v)
#         count += 1
#         tmp = 0
#         mark[v] = c
#         for u in d[v]:
#             # print('v: ', v, ' ,u: ', u)
#             if not mark[u]:
#                 tmp = dfs(u, -c, count)
#             else:
#                 if mark[v] == mark[u]:
#                     # print('debug')
#                     # print(mark)
#                     return 0
#         return max(tmp, count)

#     g = []
#     for i in range(n):
#         if not mark[i]:
#             g.append(dfs(i, 1, 0))
#     if len(g) == 0 or 0 in g:
#         print(0)
#         return

#     if len(g) == 1:
#         print(mark.count(1) * mark.count(-1) - m)
#         return

#     result = 0
#     total = n
#     for val in g:
#         total -= val
#         result += val * total
#     print(result)


# if __name__ == '__main__':
#     main()
