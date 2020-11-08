import copy
h, w, n, m = list(map(int, input().split()))
A = [[None for j in range(w)]for i in range(h)]

ab = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    A[a][b] = 'l'
    ab.append((a, b))

for _ in range(m):
    c, d = list(map(int, input().split()))
    c -= 1
    d -= 1
    A[c][d] = 'w'


B = copy.deepcopy(A)

for a, b in ab:
    target = A[a][b]
    if target == 'll':
        continue
    for k in range(b-1, -1, -1):
        if A[a][k] == 'w':
            break
        else:
            A[a][k] = 'll'
    for k in range(b, w):
        if A[a][k] == 'w':
            break
        else:
            A[a][k] = 'll'

for a, b in ab:
    target = B[a][b]
    if target == 'll':
        continue
    for k in range(a-1, -1, -1):
        if B[k][b] == 'w':
            break
        else:
            B[k][b] = 'll'
    for k in range(a, h):
        if B[k][b] == 'w':
            break
        else:
            B[k][b] = 'll'

# for row in A:
#     print(*row)

# for row in B:
#     print(*row)

result = 0
for i in range(h):
    for j in range(w):
        if A[i][j] == 'll' or B[i][j] == 'll':
            result += 1

print(result)
