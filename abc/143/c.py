N = int(input())
S = input()

count = 0
before = None
for c in S:
    if c != before:
        count += 1
    before = c

print(count)
