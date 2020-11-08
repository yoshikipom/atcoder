n = int(input())
A = list(map(int, input().split()))

power = 0
result = 1
for k in range(2, 1001):
    tmp_power = 0
    for a in A:
        if a % k == 0:
            tmp_power += 1
    if tmp_power >= power:
        # print(tmp_power, power, k)
        power = tmp_power
        result = k

print(result)
