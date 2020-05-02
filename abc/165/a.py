K = int(input())
A, B = list(map(int, input().split()))

result = False
for num in range(A, B+1):
    if num % K == 0:
        result = True

if result:
    print('OK')
else:
    print('NG')
