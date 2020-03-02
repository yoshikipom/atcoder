A = []
for i in range(3):
    Ai = [int(x) for x in input().split()]
    A.append(Ai)

N = int(input())

B = []
for i in range(N):
    b = int(input())
    B.append(b)

for i in range(3):
    for j in range(3):

        if A[i][j] in B:
            A[i][j] = -1
Bingo = [
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]],
]

result = False
for bingo in Bingo:
    count = 0
    for i, j in bingo:
        if A[i][j] == -1:
            count += 1

    if count == 3:
        result = True

if result:
    print('Yes')
else:
    print('No')
