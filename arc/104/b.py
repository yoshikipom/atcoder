N, S = input().split()
N = int(N)

As = [0]
Ts = [0]
Cs = [0]
Gs = [0]

for i in range(N):
    As.append(As[-1] + 1 if S[i] == 'A' else As[-1])
    Ts.append(Ts[-1] + 1 if S[i] == 'T' else Ts[-1])
    Cs.append(Cs[-1] + 1 if S[i] == 'C' else Cs[-1])
    Gs.append(Gs[-1] + 1 if S[i] == 'G' else Gs[-1])

result = 0
for width in range(1, N+1):
    for start in range(N+1 - width):
        cnt_a = As[start+width] - As[start]
        cnt_t = Ts[start+width] - Ts[start]
        cnt_c = Cs[start+width] - Cs[start]
        cnt_g = Gs[start+width] - Gs[start]
        if cnt_a == cnt_t and cnt_c == cnt_g:
            # print(S[start:start+width], cnt_a, cnt_t, cnt_c, cnt_g)
            result += 1

print(result)
