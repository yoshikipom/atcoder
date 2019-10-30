N = int(input())
V = list(map(int, input().split()))
V.sort()

for i in range(0, N-1):
    tmp = (V.pop(0) + V.pop(0)) / 2
    V.append(tmp)
    V.sort()

print(V[0])
