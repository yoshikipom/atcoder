import copy

N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append(a)

S = copy.deepcopy(A)
S.sort()

first = S[-1]
second = S[-2]

for a in A:
    if a == first:
        print(second)
    else:
        print(first)
