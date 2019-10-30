N = int(input())
H = list(map(int, input().split()))

result = 0
count = 0
before = 0
for i in range(N):
    now = H[i]
    if now <= before:
        count += 1
    else:
        if count > result:
            result = count
        count = 0
    before = now

if count > result:
    result = count

print(result)
