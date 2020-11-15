n, w = list(map(int, input().split()))
water = [0 for _ in range(2 * (10**5)+1)]
for _ in range(n):
    s, t, p = list(map(int, input().split()))
    water[s] += p
    water[t] -= p

cur = 0
water2 = [0 for _ in range(2 * (10**5)+1)]
for i in range(2 * (10**5)+1):
    cur += water[i]
    water2[i] = cur

# print(water)
# print(water2)
if max(water2) > w:
    print('No')
else:
    print('Yes')
