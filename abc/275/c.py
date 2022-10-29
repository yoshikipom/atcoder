import itertools


def is_square(X, Y, M):
    V = []
    for i in range(4):
        for j in range(i + 1, 4):
            if M[X[i]][Y[i]] != "#" or M[X[j]][Y[j]] != "#":
                return False
            dx = X[i] - X[j]
            dy = Y[i] - Y[j]
            V.append(dx**2 + dy **2)
    V.sort()
    l = V[0]
    if (l == 0):
        return False
    return V[0] == l and V[1] == l and V[2] == l and V[3] == l and V[4] == l * 2 and V[5] == l * 2


def main():
    M = []
    for i in range(9):
        M.append(input())

    # for row in M:
    #     print(*row)

    L = []
    for i in range(9):
        for j in range(9):
            L.append((i, j))

    count = 0
    for points in itertools.combinations(L, 4):
        X = []
        Y = []
        for point in points:
            X.append(point[0])
            Y.append(point[1])
        if is_square(X, Y, M):
            count += 1
            # print(points)

    print(count)



if __name__ == '__main__':
    main()
