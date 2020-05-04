import itertools


def calc(num):
    abs_result = abs(num) ** (1/5)
    if num < 0:
        return int(-abs_result)
    else:
        return int(abs_result)


X = int(input())

s = set()
for i in range(0, 150):
    s.add(i**5)
    s.add(-i**5)

for comb in itertools.combinations(s, 2):
    if comb[0] - comb[1] == X:
        A = calc(comb[0])
        B = calc(comb[1])
        print(A, B)
        break
    if comb[1] - comb[0] == X:
        A = calc(comb[1])
        B = calc(comb[0])
        print(A, B)
        break
