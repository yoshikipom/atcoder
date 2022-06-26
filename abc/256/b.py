from ast import For


n = input()
A = list(map(int, input().split()))

p = 0
items = []
for a in A:
    items.append(0)
    for i in range(len(items)):
        items[i] += a

for item in items:
    if item >= 4:
        p += 1

print(p)
