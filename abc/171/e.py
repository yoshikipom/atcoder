N = int(input())
A = list(map(int, input().split()))

all_xor = 0
for a in A:
    all_xor ^= a

results = []

for a in A:
    results.append(str(all_xor ^ a))

print(' '.join(results))
