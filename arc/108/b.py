n = int(input())
s = input()
t = ''

cnt = 0
for i in range(n):
    c = s[i]
    t += c
    if len(t) < 3:
        continue
    if t[-3] == 'f' and t[-2] == 'o' and t[-1] == 'x':
        cnt += 1
        t = t[0:-3]

print(n - 3 * cnt)
