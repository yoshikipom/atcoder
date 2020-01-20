H = int(input())
W = int(input())
N = int(input())

black = 0
result = 0
while black < N:
    if W < 0 or H < 0:
        print('error. W and H should be more tham 0')
        break

    if H > W:
        black += H
        W -= 1
    else:
        black += W
        H -= 1
    result += 1

print(result)
