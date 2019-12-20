import math

S = input()

count = 0
for i in range(math.floor(len(S)/2)):
    if S[i] != S[-i-1]:
        count += 1

print(count)
