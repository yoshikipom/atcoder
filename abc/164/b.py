import math
a, b, c, d = list(map(int, input().split()))

turn_a = math.ceil(c / b)
turn_b = math.ceil(a / d)

# print(turn_a)
# print(turn_b)

if turn_b < turn_a:
    print('No')
else:
    print('Yes')
