n = int(input())
A = list(map(int, input().split()))

result = - float('inf')
tmp_result = 0
tmp_sum = 0
peak = 0
for a in A:
    tmp_sum += a
    peak = max(peak, tmp_sum)
    result = max(result, tmp_result + peak)
    tmp_result += tmp_sum
    # print(tmp_sum, tmp_result, result, peak)

print(result)
