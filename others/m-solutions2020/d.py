N = int(input())
A = list(map(int, input().split()))

money = 1000
stock = 0
for i in range(N-1):
    # print(money, stock)
    if A[i] < A[i+1]:
        # 明日あがるなら買えるだけ買う
        buy = money // A[i]
        stock += buy
        money -= A[i] * buy
    elif A[i] == A[i+1]:
        # 変わらないなら何もしない
        pass
    else:
        # 明日下がるなら全部売る
        sell = stock
        stock = 0
        money += A[i] * sell

sell = stock
stock = 0
money += A[-1] * sell

print(money)
