n = int(input())
P = list(map(int, input().split()))

result = 0
used = set()
cur = 0
for p in P:
    used.add(p)
    # print(result, used)
    if p == result:
        while result in used:
            result += 1
    print(result)
