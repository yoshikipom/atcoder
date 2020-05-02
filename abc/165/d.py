def calc(x):
    return (A * x) // B - A * (x // B)


A, B, N = list(map(int, input().split()))

x = 0
if N >= B:
    x = B-1
else:
    x = N

print(calc(x))
