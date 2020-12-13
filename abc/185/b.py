n, m, T = list(map(int, input().split()))
ab = []
can = True
t = 0
battery = n
for i in range(m):
    # print('----turn:' + str(i))
    # print(battery)
    a, b = list(map(int, input().split()))
    battery -= a-t
    if battery <= 0:
        can = False
    # print(battery)
    battery += b-a
    if battery > n:
        battery = n
    # print(battery)
    t = b

battery -= T-t
# print(battery)
if battery <= 0:
    can = False


if can:
    print('Yes')
else:
    print('No')
