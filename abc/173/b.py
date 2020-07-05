AC = 0
WA = 0
TLE = 0
RE = 0

N = int(input())
for _ in range(N):
    s = input()
    if s == 'AC':
        AC += 1
    elif s == 'WA':
        WA += 1
    elif s == 'TLE':
        TLE += 1
    elif s == 'RE':
        RE += 1

print('AC', 'x', AC)
print('WA', 'x', WA)
print('TLE', 'x', TLE)
print('RE', 'x', RE)
