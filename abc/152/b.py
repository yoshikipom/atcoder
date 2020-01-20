L = []
a, b = map(int, input().split())

L.append(str(a) * b)
L.append(str(b) * a)

L.sort()

print(L[0])
