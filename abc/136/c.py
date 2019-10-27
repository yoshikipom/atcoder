N = int(input())
H = list(map(int, input().split()))

H[0] -= 1
result = True
for i in range(1, N):
    diff = H[i] - H[i-1]
    # print('i:{}, diff:{}'.format(i, diff))
    if diff < 0:
        result = False
        break
    elif diff == 0:
        pass
    elif 0 < diff:
        H[i] -= 1

if(result):
    print('Yes')
else:
    print('No')
# print(H)
