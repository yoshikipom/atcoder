N = int(input())
MONSTER = list(map(int, input().split()))
HERO = list(map(int, input().split()))

count = 0

for i in range(N):
    battle = min(HERO[i], MONSTER[i])
    count += battle
    HERO[i] -= battle
    MONSTER[i] -= battle

    if HERO[i] > 0:
        battle = min(HERO[i], MONSTER[i+1])
        count += battle
        HERO[i] -= battle
        MONSTER[i+1] -= battle


print(count)
