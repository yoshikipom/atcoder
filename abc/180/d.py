x, y, a, b = list(map(int, input().split()))

exp = 0
while True:
    # print(x, exp)
    if x >= y:
        exp -= 1
        break
    delta = x * (a - 1)
    if delta >= b:
        break

    x *= a
    exp += 1

if x < y:
    # print(y-x, exp)
    exp += (y - 1 - x) // b

print(exp)
