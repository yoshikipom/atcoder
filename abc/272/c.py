import sys

n = int(input())
A = list(map(int, input().split()))

even_list = []
odd_list = []

for a in A:
    if a % 2 == 0:
        even_list.append(a)
    else:
        odd_list.append(a)

even_list.sort()
odd_list.sort()

# print(even_list)
# print(odd_list)

if len(even_list) <= 1 and len(odd_list) <=1:
    print(-1)
elif len(even_list) <= 1:
    odd_max = odd_list[-1] + odd_list[-2]
    print(odd_max)
elif len(odd_list) <= 1:
    even_max = even_list[-1] + even_list[-2]
    print(even_max)
else:
    odd_max = odd_list[-1] + odd_list[-2]
    even_max = even_list[-1] + even_list[-2]
    print(max(even_max, odd_max))
