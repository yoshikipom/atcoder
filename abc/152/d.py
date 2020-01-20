A = [[0 for i in range(10)] for j in range(10)]
N = int(input())

result = 0
for i in range(1, N+1):
    s = str(i)
    f = int(s[0])
    l = int(s[-1])
    A[f][l] += 1
    # print('i:{} f:{}, l:{}'.format(i, f, l))

# print(A)

result = 0
for i in range(1, 10):
    for j in range(1, 10):
        result += A[i][j] * A[j][i]
        # print('debug i:{}, j:{}'.format(i, j))
        # print(result)

print(result)
