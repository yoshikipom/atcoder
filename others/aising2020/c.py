results = [0 for i in range(10**5)]
for i in range(1, 10**2):
    for j in range(1, 10**2):
        for k in range(1, 10**2):
            n = i*i + j*j + k*k + i*j + j*k + k*i
            results[n] += 1

N = int(input())
for i in range(1, N+1):
    print(results[i])
